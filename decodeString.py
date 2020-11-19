def decodeString(s):
    stack = []
    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = len(s)
    i = 0
    while i < n:
        if not s[i] == ']':
            stack.append(s[i])
        else:
            chars = []
            while not stack[-1] == '[':
                ch = stack.pop()
                chars.insert(0, ch)
            stack.pop() # '[' character
            numRep = 0
            mul = 1
            while stack and stack[-1] in integers:
                num = int(stack.pop())
                numRep = numRep + num*mul
                mul *= 10
            ans = []

            for _ in range(numRep):
                ans.extend(chars)
            for ch in ans:
                stack.append(ch)

        i += 1

    return ''.join(stack)
