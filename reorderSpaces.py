def reorderSpaces(text):
    spaces = text.count(" ")
    words = text.strip().split()
    numWords = len(words)
    if numWords == 1:
        space = ''.join([' ' for _ in range(spaces)])
        return '{}{}'.format(words[0], space)
    eachSpaceNum = spaces//(numWords-1)
    eachSpace = ''.join([' ' for _ in range(eachSpaceNum)])
    leftOverSpaceNum = spaces%(numWords-1)
    leftOverSpace = ''.join([' ' for _ in range(leftOverSpaceNum)])
    return '{}{}'.format(eachSpace.join(words), leftOverSpace)
