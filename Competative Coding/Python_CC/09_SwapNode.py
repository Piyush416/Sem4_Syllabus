# Write a Program to Swap Nodes pairwise

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
        
 
def Print(n1):
    while n1 != None:
        print(n1.data,end="->")
        n1 = n1.next
    print("None")


def SwapNode(n1):
    
    while n1 != None:
        a = n1.data
        if n1.next == None:
            return
        n1.data = n1.next.data
        n1 = n1.next
        n1.data = a
        n1 = n1.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)

print("Given Linked List")
Print(a)
print('\nSwapped Linked List')
SwapNode(a)
Print(a)