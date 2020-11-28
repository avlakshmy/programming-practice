def isValidParenthesis(parenthesisString):
    if len(parenthesisString) == 0:
        return True
    stack = []
    for letter in parenthesisString:
        if len(stack) == 0:
            if letter == ')':
                return False
            else:
                stack.append(letter)
        else:
            if letter == '(':
                stack.append(letter)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False

def generateAllParentheses(parenthesesLength):
    if parenthesesLength == 1:
        return ['(', ')']
    answer = []
    poss = generateAllParentheses(parenthesesLength-1)
    answer.extend(['(' + x for x in poss])
    answer.extend([')' + x for x in poss])
    return answer

def generateParenthesis(n):
    possibleParentheses = generateAllParentheses(2*n)

    validParentheses = []
    for candidateParenthesis in possibleParentheses:
        if isValidParenthesis(candidateParenthesis):
            validParentheses.append(candidateParenthesis)

    return validParentheses
