# Write a Program to Understand and implement Tree traversals i.e. Pre-Order Post-Order, In-Order


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val,end=" ")
        print_inorder(root.right)
      
        
def print_preorder(root):
    if root:
        print(root.val, end = ' ')
        print_preorder(root.left)
        print_preorder(root.right)
        
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val, end = ' ')
        
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal of binary tree is: ")
print_inorder(root)

print("\nPreorder Traversal of binary tree is: ")
print_preorder(root)

print("\nPostorder Traversal of binary tree is: ")
print_postorder(root)

