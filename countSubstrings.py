def differByOne(s1, s2):
    ans = [s1[i] == s2[i] for i in range(len(s1))]
    if ans.count(False) == 1:
        return True
    return False
    
def countSubstrings(s, t):
    count = 0
    s1s = []
    s2s = []
    for si in range(0, len(s)):
        for sj in range(si+1, len(s)+1):
            s1s.append(s[si:sj])
    s1sdict = {}
    for s1str in s1s:
        if s1str in s1sdict:
            s1sdict[s1str] += 1
        else:
            s1sdict[s1str] = 1
    for ti in range(0, len(t)):
        for tj in range(ti+1, len(t)+1):
            s2s.append(t[ti:tj])
    s2sdict = {}
    for s2str in s2s:
        if s2str in s2sdict:
            s2sdict[s2str] += 1
        else:
            s2sdict[s2str] = 1
    for s1, s1freq in s1sdict.items():
        for s2, s2freq in s2sdict.items():
            if len(s1) == len(s2) and differByOne(s1, s2):
                count += (s1freq*s2freq)
    return count
