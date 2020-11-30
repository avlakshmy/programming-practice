def gcdOfStrings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len2 > len1:
        str1, str2, len1, len2 = str2, str1, len2, len1
    i = 0
    j = 0
    while i < len(str1) and j < len(str2) and str1[i] == str2[j]:
        i += 1
        j += 1
    if i == len1:
        return str2
    if j == len(str2):
        return self.gcdOfStrings(str2, str1[i:])
    return ""
