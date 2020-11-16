def hasPathSum(root, sumVal):
    if root == None:
        return False
    if root.left == None and root.right == None:
        if root.val == sumVal:
            return True
        return False
    return hasPathSum(root.left, sumVal - root.val) or hasPathSum(root.right, sumVal - root.val)
            
def pathSum(root, sumVal):
    if root == None:
        return []
    if root.left == None and root.right == None:
        if root.val == sumVal:
            return [[root.val]]
        return []
    if hasPathSum(root, sumVal):
        paths = []
        if hasPathSum(root.left, sumVal - root.val):
            lpaths = self.pathSum(root.left, sumVal - root.val)
            for path in lpaths:
                paths.append([root.val] + path)
        if hasPathSum(root.right, sumVal - root.val):
            rpaths = self.pathSum(root.right, sumVal - root.val)
            for path in rpaths:
                paths.append([root.val] + path)
        return paths
    return []
