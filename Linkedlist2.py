class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, pos):
        temp = self.head
        count = 0
        while temp:
            if count == pos:
                return temp.data
            temp = temp.next
            count += 1
        return None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next   
            curr.next = prev      
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.display()
ll.reverse()
ll.display()
