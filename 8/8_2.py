import numpy
with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


global rows
rows = len(lines)
global cols 
cols = len(lines[0])


def viewing_distance(row, col, lines):
    value = lines[row][col]
    dist = []

    all_down = []
    test = 0
    for i in range(1, rows):
        down = [row+i, col]
        if int(down[0]) < rows:
            all_down.append(down)
    for d in all_down:
        if lines[d[0]][d[1]] < value:
            test+=1
        else:
            test+=1
            break
    dist.append(test)

    #up
    all_up = []
    test = 0
    for i in range(1, rows):
        up = [row-i, col]
        if int(up[0]) >= 0:
            all_up.append(up)
    for u in all_up:
        if lines[u[0]][u[1]] < value:
            test+=1
        else:
            test+=1
            break
    dist.append(test)

    #right
    all_right = []
    test = 0
    for j in range(1, cols):
        right = [row, col+j]
        if int(right[1]) < cols:
            all_right.append(right)
    for r in all_right:
        if lines[r[0]][r[1]] < value:
            test+=1
        else:
            test+=1
            break
    dist.append(test)

    #left
    all_left = []
    test = 0
    for j in range(1, cols):
        left = [row, col-j]
        if int(left[1]) >= 0:
            all_left.append(left)
    for l in all_left:
        if lines[l[0]][l[1]] < value:
            test+=1
        else:
            test+=1
            break
    dist.append(test)
    return numpy.prod(dist)

scenic_scores = []
for i in range(1, rows-1):
    for j in range(1, cols-1):
        scenic_scores.append(viewing_distance(i, j, lines))

print(max(scenic_scores))
