def compress(chars):
    ans = []
    count = 1
    currchar = chars[0]
    i = 1
    while i < len(chars):
        if chars[i] == currchar:
            count += 1
        else:
            ans.append((currchar,count))
            currchar = chars[i]
            count = 1
        i += 1
    ans.append((currchar,count))
    chars[:] = []
    for tup in ans:
        chars.append(tup[0])
        if tup[1] > 1:
            freq = list(str(tup[1]))
            chars.extend(freq)
    return len(chars)
