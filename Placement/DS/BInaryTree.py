#l<root
#r>=root
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data,ref):
        if self.root is None:
            self.root=Node(data)
        else:
            new_node=Node(data)
            if data<ref.data:
                if ref.left is not None:
                    self.insert(data,ref.left)
                else:
                    ref.left=new_node
            else:
                if ref.right is not None:
                    self.insert(data,ref.right)
                else:
                    ref.right=new_node

    def inorder(self,ref):
        if ref:
            self.inorder(ref.left)
            print(ref.data,end=' ')
            self.inorder(ref.right)

    def preorder(self,ref):
        if ref:
            print(ref.data,end=' ')
            self.preorder(ref.left)
            self.preorder(ref.right)

    def postorder(self,ref):
        if ref:
            self.postorder(ref.left)
            self.postorder(ref.right)
            print(ref.data,end=' ')
 


bt=BinaryTree()
bt.insert(5,bt.root)
bt.insert(4,bt.root)
bt.insert(6,bt.root)
bt.insert(9,bt.root)
bt.insert(2,bt.root)
bt.insert(12,bt.root)
bt.insert(10,bt.root)

bt.inorder(bt.root)
print('\n')
bt.preorder(bt.root)
print('\n')
bt.postorder(bt.root)
print('\n')