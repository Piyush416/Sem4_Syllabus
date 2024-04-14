# Write a Program for Building a Function ISVALID to VALIDATE BST
import sys

class Node:
  def __init__(self,d):
    self.data = d
    self.left = None
    self.right = None

INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize


def isBST(root):
  return isBstCheck(root,INT_MIN,INT_MAX)
  

def isBstCheck(node,mini,maxi):
  if node is None:
    return True
    
  if node.data < mini or node.data > maxi:
    return False
    
  if (isBstCheck(node.left,mini,node.data-1) and isBstCheck(node.right,node.data+1,maxi)):
    return True
  
a = Node(4)
a.left = Node(2)
a.right = Node(5)
a.left.left = Node(1)
a.left.right = Node(3)

if isBST(a):
  print("Valid BST")
else:
  print("Not Valid")


  