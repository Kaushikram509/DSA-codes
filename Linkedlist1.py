class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end (FIXED)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at position
    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Search
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Get element by index (ADDED)
    def get(self, index):
        temp = self.head
        count = 0

        while temp:
            if count == index:
                return temp.data
            temp = temp.next
            count += 1

        return None

    # Display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Driver code
ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()

ll.insert_at_position(2, 15)
ll.display()

print(ll.get(0))
print(ll.get(1))

print(ll.search(20))

ll.delete_from_beginning()
ll.display()

ll.delete_from_end()
ll.display()
