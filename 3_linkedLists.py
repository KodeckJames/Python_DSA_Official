# llstr = linked list string
class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data, None)

    def insert_values(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("This is not a valid index")
        
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

if __name__=='__main__':
    ll=LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(79)
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    print(f"Length: {ll.get_length()}")
    ll.remove_at(2)
    ll.print()
    ll.insert_at(0,"figs")
    ll.print()
    ll.insert_at(2,"Jackfruit")
    ll.print()

#EASIER IMPLEMENTATION OF THE LINKED LIST
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# def __str__(self): is a special function in a class that tells Python what to show when you print the object.

# To make a linked list, you generally have reference only to the head:
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

# Traverse the list - O(n)
curr = Head

while curr:
    print(curr)
    curr = curr.next


# Display the linked list
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("->".join(elements))


display(Head)


# Search for a node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


print(search(Head, 7))
