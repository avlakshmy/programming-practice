def numberOfLines(widths, S):
    lines = 0
    prevLineLength = 0
    currLineLength = 0
    i = 0
    while i < len(S):
        if currLineLength + widths[ord(S[i]) - ord('a')] <= 100:
            currLineLength += widths[ord(S[i]) - ord('a')]
        else:
            lines += 1
            prevLineLength = currLineLength
            currLineLength = widths[ord(S[i]) - ord('a')]
        i += 1
    if currLineLength == 0:
        return [lines, prevLineLength]
    return [lines+1, currLineLength]
