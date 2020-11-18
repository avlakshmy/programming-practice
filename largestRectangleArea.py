def largestRectangleArea(heights):
    if len(heights) == 0:
        return 0
    maxArea = 0
    stack = [[0,heights[0]]]
    for i in range(1, len(heights)):
        if heights[i] >= stack[-1][1]:
            stack.append([i, heights[i]])
        else:
            while len(stack) > 0 and stack[-1][1] > heights[i]:
                top = stack.pop()
                currArea = (i - top[0]) * top[1]
                if currArea > maxArea:
                    maxArea = currArea
            stack.append([top[0], heights[i]])
    while len(stack) > 0:
        top = stack.pop()
        currArea = (len(heights) - top[0]) * top[1]
        if currArea > maxArea:
            maxArea = currArea
    return maxArea
