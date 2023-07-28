class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
     # Creating a new node
        new_node = Node(val)
    
     # Case 1: Root is None
        if self.root is None:
            self.root = new_node
            return
    
        temp = self.root
    # Traverse using while loop 
        while temp:
        # Case 2: Value is lesser
            if val < temp.info:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
        # Case 3 Value is greater
            else:
                if temp.right is None:
                    temp.right = new_node
                    return 
                temp = temp.right
                    
         
         

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
