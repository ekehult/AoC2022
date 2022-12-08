with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


global rows
rows = len(lines)
global cols 
cols = len(lines[0])
global tot_visible 
tot_visible = 2*(rows - 1) + 2*(cols-1)


def visible(row, col, lines):
    all_down = []
    test = 0
    for i in range(1, rows):
        down = [row+i, col]
        if int(down[0]) < rows:
            all_down.append(down)
    for d in all_down:
        if int(lines[d[0]][d[1]]) < int(lines[row][col]):
            test+=1
    if test == len(all_down):
        return True

    #up
    all_up = []
    test = 0
    for i in range(1, rows):
        up = [row-i, col]
        if int(up[0]) >= 0:
            all_up.append(up)
    for u in all_up:
        if lines[u[0]][u[1]] < lines[row][col]:
            test+=1
    if test == len(all_up):
        return True

    #right
    all_right = []
    test = 0
    for j in range(1, cols):
        right = [row, col+j]
        if int(right[1]) < cols:
            all_right.append(right)
    for r in all_right:
        if lines[r[0]][r[1]] < lines[row][col]:
            test+=1
    if test == len(all_right):
        return True

    #left
    all_left = []
    test = 0
    for j in range(1, cols):
        left = [row, col-j]
        if int(left[1]) >= 0:
            all_left.append(left)
    for l in all_left:
        if lines[l[0]][l[1]] < lines[row][col]:
            test+=1
    if test == len(all_left):
        return True
    return False


for i in range(1, rows-1):
    for j in range(1, cols-1):

        if visible(i, j, lines):
            tot_visible+=1
            
            

print(tot_visible)