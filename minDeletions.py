def minDeletions(s):
    freq = [0 for _ in range(26)]
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    freq.sort(reverse=True)
    if 0 in freq:
        non_zero_freq = freq[:freq.index(0)]
    else:
        non_zero_freq = freq[:]

    freq_count = {}
    for freq in non_zero_freq:
        if freq in freq_count:
            freq_count[freq] += 1
        else:
            freq_count[freq] = 1

    numDels = 0
    while not all([count == 1 for count in freq_count.values()]):
        for freq, count in freq_count.items():
            if count > 1:
                break
        freq_count[freq] -= 1
        numDels += 1
        if freq > 1:
            if freq-1 in freq_count:
                freq_count[freq-1] += 1
            else:
                freq_count[freq-1] = 1

    return numDels
