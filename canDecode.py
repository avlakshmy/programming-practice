def canDecode(bits):
    if len(bits) == 1:
        if bits[0] == 0:
            return True
        return False
    if len(bits) == 2:
        if bits == [0,1]:
            return False
        return True
    if bits[-2:] == [0,1]:
        return False
    if bits[-2:] == [1,1]:
        return canDecode(bits[:-2])
    return canDecode(bits[:-2]) or canDecode(bits[:-1])
    
def isOneBitCharacter(bits):
    if len(bits) == 1:
        return True
    if len(bits) == 2:
        if bits[0] == 1:
            return False
        return True
    if canDecode(bits[:-1]):
        return True
    return False
            
        
