class Node:
    def __init__(self,d):
        self.left = None
        self.right = None
        self.val = d
        
        
def are_mirror(a, b):
    
    if a is None and b is None:
        return True
    
    if a is None or b is None:
        return False
        
    if ( (a.val == b.val) and are_mirror(a.left,b.right) and are_mirror(a.right,b.left) ):
        return True

root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)


if are_mirror(root1, root2):
    print("Yes")
else:
    print("No")