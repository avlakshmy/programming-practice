def findSumAndTilt(root):
    if root == None:
        return 0, 0
    leftSum, leftTilt = findSumAndTilt(root.left)
    rightSum, rightTilt = findSumAndTilt(root.right)
    totSum = root.val + leftSum + rightSum
    totTilt = leftTilt + rightTilt + abs(leftSum - rightSum)
    return totSum, totTilt

def findTilt(root):
    sumval, tilt = findSumAndTilt(root)
    return tilt
