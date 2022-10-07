#Creating and inserting elements in inoder
#in Inorder, you first visit the left, then root and finally right. 


class Node:  # creating a node with left having none, data having value and right having none
    def __init__(self,value):
        self.left=None 
        self.data=value
        self.right=None
    
class Tree: #creating a tree 
    def CreateNode(self,data):           #function to create the first node(root) of the tree, it takes one parameter; data
        return Node(data)                #assigning a value to the Node created

    def insert(self,node,data):          # function to insert elements to nodes
        if node is None:                  #checking if the root node contains an element or number
            return self.CreateNode(data)  # assigning element in the created node if it is empty
        if data < node.data:              #assigning elements(child node) to the parent node basing on the condition 
            node.left= self.insert(node.left,data) #assign to left if element is < than parent node
        else:
            node.right=self.insert(node.right,data)   #assign to right if element is > than parent node
        return node 
    
    
#To print elements in order use the traverse function    
    def traverse_Inorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data)
            self.traverse_Inorder(root.right)
         
#Driver code
tree=Tree() # assigning Tree() to avariable tree
root=tree.CreateNode(5) #assigning value to root node(CreateNode) and then assign to a variable called root
print(root.data) # printing value or element at the root node


#inserting more elements on the right and left of the tree basing on the conditions 
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

print("Inorder---->")
tree.traverse_Inorder(root)