class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None      #Initializing left node and right to None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

root = BST(10)
list1 = [20,10,4,56,32,12,45,3,5,56,100,50,999,1000]
for i in list1:
    root.insert(i)
