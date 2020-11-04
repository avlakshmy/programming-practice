def withinAnHour(t1,t2,t3):
    t1 = [int(x) for x in t1.split(':')]
    t2 = [int(x) for x in t2.split(':')]
    t3 = [int(x) for x in t3.split(':')]
    t1_num = t1[0]*60 + t1[1]
    t2_num = t2[0]*60 + t2[1]
    t3_num = t3[0]*60 + t3[1]
    if t1_num < t2_num and t2_num < t3_num and t3_num - t1_num <= 60:
        return True
    return False
    
def alertNames(keyName, keyTime):
    users = {}
    for name,time in zip(keyName,keyTime):
        if name in users:
            users[name].append(time)
        else:
            users[name] = [time]
    ans = set()
    for name,times in users.items():
        if len(times) >= 3:
            times.sort()
            count = 0
            i = 0
            while i < len(times)-2:
                if withinAnHour(times[i],times[i+1],times[i+2]):
                    ans.add(name)
                i += 1
    ans = list(ans)
    ans.sort()
    return ans      
                
