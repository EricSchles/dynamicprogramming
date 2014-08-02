#tree of randomly generated values
import random

class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = None
        self.right = None
    
    def __str__(self):
        return repr(self.item)

class Tree:
    def __init__(self):
        self.root = Node(random.randint(0,1000))
    
    def initialize_tree(self,tree_depth):
        if tree_depth <= 0:
            print "specify a positive depth"
            return None
        else:
            return self._initialize_tree(tree_depth,self.root)

    def _initialize_tree(self,tree_depth,curr):
        if tree_depth == 0:
            return True
        else:
            left = Node(random.randint(0,1000))
            right = Node(random.randint(0,1000))
            curr.left = left
            curr.right = right
            self._initialize_tree(tree_depth-1,curr.left)
            self._initialize_tree(tree_depth-1,curr.right)
    
    def pretty_print(self):
        self._pretty_print(self.root,0)
    
    def _pretty_print(self,curr,level):
        if curr == None:
            return True
        else:
            if curr.left != None:
                self._pretty_print(curr.left,level+1)
            
            print (" "*level)+str(curr.item)
            if curr.right != None:
                self._pretty_print(curr.right,level+1)
            
    def clear(self):
        self.root.left = None
        self.root.right = None
        self.root = Node(random.randint(0,1000))

class solver:
    #root is the root of the tree being passed in
    def __init__(self,root):
        self.array = []
        self.root = root
    
    def minpath(self):
        if self.root == None:
            print "Please provide a non-empty tree"
        else:
            return self._minpath(self.root.item,self.root)
    
    def _minpath(self,parent,curr):
        curr.item += parent
        #assumes tree is complete, change this to "or" if incomplete tree
        if curr.left == None and curr.right == None:
            self.array.append(curr.item)
        else:
            self._minpath(curr.item,curr.left)
            self._minpath(curr.item,curr.right)

    def mincost(self):
        self.minpath()
        return min(self.array)

    
