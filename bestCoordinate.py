import math
def bestCoordinate(towers, radius):
    xmin = min([tower[0] for tower in towers])
    xmax = max([tower[0] for tower in towers])
    ymin = min([tower[1] for tower in towers])
    ymax = max([tower[1] for tower in towers])
    x_best = xmin
    y_best = ymin
    best_score = 0
    for tower in towers:
        dist = math.sqrt((x_best - tower[0])*(x_best - tower[0]) + (y_best - tower[1])*(y_best - tower[1]))
        if dist <= radius:
            best_score += math.floor(tower[2]/(1 + dist))
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            score = 0
            for tower in towers:
                dist = math.sqrt((x - tower[0])*(x - tower[0]) + (y - tower[1])*(y - tower[1]))
                if dist <= radius:
                    score += math.floor(tower[2]/(1 + dist))
            if score > best_score:
                x_best = x
                y_best = y
                best_score = score

    return [x_best, y_best]
