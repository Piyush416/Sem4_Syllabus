#  Write a Program to find the Merge point of two linked lists(sorted) Using HashSet in this 
class Node:
  def __init__(self,d):
    self.data = d;
    self.next = None

def Print(n):
  while n != None:
    print(n.data,end="->")
    n = n.next
    

def MegeNode(n1,n2):
  hs = set()
  
  while n1 != None:
    hs.add(n1)
    n1 = n1.next
  
  while n2 != None:
    if n2 in hs:
      return print(n2.data)
    n2=n2.next

  return None
 
# Function to print the list
def Print(n):
    cur = n;
    while (cur != None) :
        print(cur.data, end=" ");
        cur = cur.next;
    print("");
 
# Function to find the intersection of two node
def MegeNode(n1, n2):
     
    # Define hashset
    hs = set();
 
    while (n1 != None):
        hs.add(n1);
        n1 = n1.next;
    while (n2 != None):
        if (n2 in hs):
            print("Intersection of two linked list is: " ,n2.data);
            return
        n2 = n2.next;
     
    return None;
 
 
 
# list 1
n1 = Node(1);
n1.next = Node(2);
n1.next.next = Node(3);
n1.next.next.next = Node(4);
n1.next.next.next.next = Node(5);
n1.next.next.next.next.next = Node(6);
n1.next.next.next.next.next.next = Node(7);
 
# list 2
n2 = Node(10);
n2.next = Node(9);
n2.next.next = Node(8);
n2.next.next.next = n1.next.next.next;

Print(n1)
Print(n2)

MegeNode(n1,n2)
