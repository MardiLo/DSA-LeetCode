class Print:
    def TreeTraversalBFS(self, root):
        from collections import deque
        
        if not root:
            return []

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

    def LinkedListTraversal(self, head):
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        return res