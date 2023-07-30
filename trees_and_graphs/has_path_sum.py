def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    
        def transverse(node, sum_here=0):
            
            if not node:
                return sum_here == target_sum
            
            sum_here += node.val
            
            if not node.left:
                return transverse(node.right, sum_here)
            if not node.right:
                return transverse(node.left, sum_here)
            else:   
                return transverse(node.left, sum_here) or transverse(node.right, sum_here)
    
        if not root:
            return False
        
        return transverse(root)
            