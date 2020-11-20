def area(x1, y1, x2, y2):
    return (y2 - y1)*(x2 - x1)

def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3:
        return None
    if x4 < x1:
        return None
    if y2 < y3:
        return None
    if y4 < y1:
        return None
    return [max(x1,x3), max(y1,y3), min(x2,x4), min(y2,y4)]

def computeArea(A, B, C, D, E, F, G, H):
    area1 = area(A, B, C, D)
    area2 = area(E, F, G, H)
    wxyz = intersection(A, B, C, D, E, F, G, H)
    if wxyz:
        W = wxyz[0]
        X = wxyz[1]
        Y = wxyz[2]
        Z = wxyz[3]
        area3 = area(W, X, Y, Z)
    else:
        area3 = 0
    return area1 + area2 - area3
