class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    def insert_at_position(self,pos,data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp= self.head
        for _ in range(pos-1):
            if(temp is None):
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next
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
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data  == key:
                return True
            temp = temp.next
        return False
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=",")
            temp = temp.next
        print("None")

ll= LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()      #5<10<20<30   #5,10,20,30,None
ll.insert_at_position(2,15)
ll.display()
print(ll.get(0))
print(ll.get(1))
print(ll.search(20))   #True
ll.delete_from_beginning()
ll.display()       #10,20,30,None
ll.delete_from_end()
ll.display()        #10,20,None
