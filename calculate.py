def evaluate(s):
    exp = []
    exp1 = s.strip().split('*')
    for part in exp1:
        exp.append(part)
        exp.append('*')
    exp.pop()
    exp2 = [x.strip().split('/') for x in exp]
    exp = []
    for part in exp2:
        if len(part) == 1:
            exp.append(part[0])
        else:
            for p in part:
                exp.append(p)
                exp.append('/')
            exp.pop()
    ans = int(exp[0])
    for i in range(1, len(exp), 2):
        op = exp[i]
        val = int(exp[i+1])
        if op == '*':
            ans = ans * val
        else:
            ans = ans // val
    return ans
    
def calculate(s):
    exp = []
    exp1 = s.strip().split('+')
    for part in exp1:
        exp.append(part)
        exp.append('+')
    exp.pop()
    exp2 = [x.strip().split('-') for x in exp]
    exp = []
    for part in exp2:
        if len(part) == 1:
            exp.append(part[0])
        else:
            for p in part:
                exp.append(p)
                exp.append('-')
            exp.pop()
    for i in range(len(exp)):
        if '*' in exp[i] or '/' in exp[i]:
            val = evaluate(exp[i])
            exp[i] = str(val)
    ans = int(exp[0])
    for i in range(1, len(exp), 2):
        op = exp[i]
        val = int(exp[i+1])
        if op == '+':
            ans = ans + val
        else:
            ans = ans - val
    return ans
