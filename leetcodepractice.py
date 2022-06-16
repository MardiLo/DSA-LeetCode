from collections import deque

class Print:
    def TreeTraversalBFS(self, root):
        """
        Collect all elements in tree by breadth-first traversal algorithm (Root -> Level 1 -> Level 2 -> ... -> Level n)
        """
        
        if not root: return []

        queue = deque([root])                                   # create a queue and initialize it by containing the root
        res = []
        while queue:
            node = queue.popleft()                              # FIFO  
            res.append(node.val)
            
            if node.left:
                queue.append(node.left)                         # collect left child if it exists
            if node.right:
                queue.append(node.right)                        # collect right child if it exists
                
        return res


    def TreeTraversalDFS(self, root):
        if not root: return []

        stack = [root]                                          # create a stack and initialize it by containing the root
        res = []
        while stack:
            node = stack.pop()                                  # LIFO  
            res.append(node.val)
            
            if node.left:
                stack.append(node.left)                         # collect left child if it exists
            if node.right:
                stack.append(node.right)                        # collect right child if it exists
                
        return res

    def TreeTraversalPreorder(self, node):
        """
        Collect all elements in tree by preorder traversal algorithm (Root -> Left -> Right)
        """
        
        if not node: return []

        res = []
        res.append(node.data)                                  # start from the root
        res += self.TreeTraversalPreorder(node.left)           # collect left child
        res += self.TreeTraversalPreorder(node.right)          # collect right child

        return res

    
    def TreeTraversalPostorder(self, node):
        """
        Collect all elements in tree by postorder traversal algorithm (Left -> Right -> Root)
        """
        
        if not node: return []

        res = []
        res += self.TreeTraversalPostorder(node.left)           # go to the leftmost child first
        res += self.TreeTraversalPostorder(node.right)          # collect right child
        res.append(node.data)                                   # back to the root

        return res
    
    
    def TreeTraversalInorder(self, node):
        """
        Collect all elements in tree by inorder traversal algorithm (Left -> Root -> Right)
        """
        
        if not node: return []

        res = []
        res += self.TreeTraversalInorder(node.left)             # go to the leftmost child first
        res.append(node.data)                                   # collect the root
        res += self.TreeTraversalInorder(node.right)            # collect right child  

        return res


    def LinkedListTraversal(self, head):
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        return res