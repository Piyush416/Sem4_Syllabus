# Write a Program to Build BST Using Given Array
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert(node, key):
	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)
	return node


def inorder(root):
	if root:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)


def preorder(node):
    if node is None:
        return
    print(node.key, end=' ')
    preorder(node.left)
    preorder(node.right)
    
def postorder(node):
  if node is None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.key,end=" ")

if __name__ == '__main__':
  
  a = [50,30,20,40,70,60,80]
  # a = [20,30,40,50,60,70,80]
  root = None
  root = insert(root, a[0])
  
  for i in range(1,7):
    insert(root, a[i])
  
  print("Inorder of BST:")
  inorder(root)
  print("\nPreorder of BST:")
  preorder(root)
  print("\nPostorder of BST:")
  postorder(root)
  
