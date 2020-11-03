def slowestKey(releaseTimes, keysPressed):
    lengths = {}
    lengths[keysPressed[0]] = releaseTimes[0]
    for i in range(1, len(keysPressed)):
        k = keysPressed[i]
        time = releaseTimes[i] - releaseTimes[i-1]
        if k in lengths:
            if time > lengths[k]:
                lengths[k] = time
        else:
            lengths[k] = time
    maxkey = keysPressed[0]
    maxtime = releaseTimes[0]
    for key,time in lengths.items():
        if time > maxtime:
            maxkey = key
            maxtime = time
        elif time == maxtime:
            if key > maxkey:
                maxkey = key
    return maxkey
