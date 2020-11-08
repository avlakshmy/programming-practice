def balancedStringSplit(s):
    same = {'L': 'L', 'R': 'R'}
    other = {'L': 'R', 'R': 'L'}
    stack = []
    count = 0
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == same[char]:
            stack.append(char)
        elif stack[-1] == other[char]:
            stack.pop()
            if len(stack) == 0:
                count += 1
    return count
