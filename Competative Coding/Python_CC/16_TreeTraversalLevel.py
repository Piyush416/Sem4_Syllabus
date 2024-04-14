# Write a Program to Traverse a Tree using Level Order Traversal
class Node:
  def __init__(self,key):
    self.data = key
    self.left = self.right = None
    
def print_level_order(root):
  h = Height(root)
  
  for i in range(1,h+1):
    print_current_level(root, i)
    

    
def print_current_level(root, level):
  if root is None:
    return
  
  if level == 1:
    print(root.data,end=" ")
  
  if level  > 1:
    print_current_level(root.left,level-1)
    print_current_level(root.right,level-1)
    

def Height(root):
  if root is None:
    return 0
  
  ldepth = Height(root.left)
  rdepth = Height(root.right)
  
  if ldepth>rdepth:
    return ldepth+1
  else:
    return rdepth+1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_level_order(root)
    