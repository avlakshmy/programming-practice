def longestPalindrome(s):
    if len(s) == 0:
        return ""
    slen = len(s)
    lpLen = 1
    lpStart = 0
    lpEnd = 0
    for i in range(slen):
        start = i
        end = i
        while start >= 1 and end <= slen-2 and s[start-1] == s[end+1]:
            start -= 1
            end += 1
        currLen = end - start + 1
        if currLen > lpLen:
            lpLen = currLen
            lpStart = start
            lpEnd = end
    for i in range(slen-1):
        start = i
        end = i+1
        if s[start] == s[end]:
            while start >= 1 and end <= slen-2 and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            currLen = end - start + 1
            if currLen > lpLen:
                lpLen = currLen
                lpStart = start
                lpEnd = end
    return s[lpStart:lpEnd+1]
