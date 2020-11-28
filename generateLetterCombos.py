def generateLetterCombinations(allPossibleCombinations):
    if len(allPossibleCombinations) == 1:
        return allPossibleCombinations[0]
    firstLetters = allPossibleCombinations[0]
    remainingLetterCombinations = generateLetterCombinations(allPossibleCombinations[1:])
    answer = []
    for letter in firstLetters:
        answer.extend([letter + combination for combination in remainingLetterCombinations])
    return answer

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    digitToLettersMap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    allPossibleCombinations = [digitToLettersMap[digit] for digit in digits]
    return generateLetterCombinations(allPossibleCombinations)
