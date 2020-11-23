def minWindow(s, t):
    if len(s) == 0 or len(t) == 0:
        return ""
    if len(t) > len(s):
        return ''
    for letter in t:
        if not letter in s:
            return ''
    tfreq = {}
    for ch in t:
        if ch in tfreq:
            tfreq[ch] += 1
        else:
            tfreq[ch] = 1
    tlen = len(t)
    slen = len(s)
    ans = ""
    left = 0
    count = 0
    minLength = math.inf
    for right in range(slen):
        if s[right] in tfreq:
            tfreq[s[right]] -= 1
            count += 1

        while count == tlen:
            if minLength > right - left + 1:
                minLength = right - left + 1
                ans = s[left:right+1]
            if s[left] in tfreq:
                count -= 1
            left += 1
    return ans    
