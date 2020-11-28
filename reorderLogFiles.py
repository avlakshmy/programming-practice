def reorderLogFiles(logs):
    if len(logs) == 0:
        return []
    letterLogs = []
    digitLogs = []
    for log in logs:
        logWords = log.split()
        if logWords[1].isnumeric():
            digitLogs.append(log)
        else:
            letterLogs.append(log)
    letterLogs.sort(key=lambda x: (' '.join(x.split()[1:]), x.split()[0]))
    answer = letterLogs + digitLogs
    return answer
