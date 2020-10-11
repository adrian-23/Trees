from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #precondition: root is not null
    def create_tree(self, values:List):
        if len(values) == 0:
            return self
        
        else:
            for value in values:
                node = TreeNode(value)
                self.level_order_insertion(node)
            
            return self
    
    def level_order_insertion(self, node:'TreeNode'):
        
        queue = [self]

        while(len(queue) != 0):
            level = len(queue)
            while(level != 0):
                explore = queue.pop()

                if explore.left == None:
                    explore.left = node
                    return
                elif explore.right == None:
                    explore.right = node
                    return
                else:
                    queue.insert(0,explore.left)
                    queue.insert(0,explore.right)                    
                
            
                level-=1
           
    def preorder(self,root):
        
        if root == None:
            return
        else:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)



