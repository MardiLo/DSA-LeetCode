from collections import deque

class Print:
    def TreeTraversalBFS(self, root) -> list:
        """Collect all elements in tree by breadth-first traversal algorithm (Root -> Level 1 -> Level 2 -> ... -> Level n)"""
        
        if not root: return []

        queue, res = deque([root]), []                          # create a queue and initialize it by containing the root
        while queue:
            root = queue.popleft()                              # FIFO  
            res.append(root.val)
            
            if root.left: queue.append(root.left)               # collect left child if it exists
            if root.right: queue.append(root.right)             # collect right child if it exists
                
        return res


    def TreeTraversalDFS(self, root) -> list:
        """Mirrow of preorder traversal, reverse of postorder traversal (Root -> Right -> Left)"""

        if not root: return []

        stack, res = [root], []                                 # create a stack and initialize it by containing the root
        while stack:
            root = stack.pop()                                  # LIFO  
            res.append(root.val)
            
            if root.left: stack.append(root.left)               # collect left child if it exists
            if root.right: stack.append(root.right)             # collect right child if it exists
                
        return res


    def TreeTraversalPreorder(self, root) -> list:
        """Collect all elements in tree by preorder traversal algorithm (Root -> Left -> Right)"""

        return [root.val] + self.TreeTraversalPreorder(root.left) + self.TreeTraversalPreorder(root.right) if root else []

    
    def TreeTraversalPostorder(self, root) -> list:
        """Collect all elements in tree by postorder traversal algorithm (Left -> Right -> Root)"""

        return self.TreeTraversalPostorder(root.left) + self.TreeTraversalPostorder(root.right) + [root.val] if root else []

    
    def TreeTraversalInorder(self, root) -> list:
        """Collect all elements in tree by inorder traversal algorithm (Left -> Root -> Right)"""

        return self.TreeTraversalInorder(root.left) + [root.val] + self.TreeTraversalInorder(root.right) if root else []


    def LinkedListTraversal(self, head) -> list:
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        return res