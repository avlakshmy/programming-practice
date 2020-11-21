def invalidTransactions(transactions):
    n = len(transactions)
    txns = []
    for tx in transactions:
        ans = tx.split(",")
        txns.append(ans)
    # name, city, time, amount
    invTxns = set()
    for i in range(n):
        if int(txns[i][2]) > 1000:
            invTxns.add(','.join(txns[i]))
        for j in range(n):
            if not i == j:
                if txns[i][0] == txns[j][0] and not(txns[i][3] == txns[j][3]) and abs(int(txns[i][1]) - int(txns[j][1])) <= 60:
                    invTxns.add(','.join(txns[i]))
                    invTxns.add(','.join(txns[j]))
    return list(invTxns)
