with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    visited = []
    H_pos = [0, 0]
    T_pos = [0, 0]

    for line in lines:
        instruction = line.split(' ')
        direction = instruction[0]
        steps = instruction[1]
        for i in range(int(steps)):
            if direction == 'U':
                H_pos = [H_pos[0]+1, H_pos[1]]
            if direction == 'D':
                H_pos = [H_pos[0]-1, H_pos[1]]
            if direction == 'R':
                H_pos = [H_pos[0], H_pos[1]+1]
            if direction == 'L':
                H_pos = [H_pos[0], H_pos[1]-1]

            # check if in same row/column
            if T_pos[0] == H_pos[0] or T_pos[1] == H_pos[1]:

                if abs(T_pos[0] - H_pos[0]) > 1:
                    #in different rows
                    # check if T is under H
                    if T_pos[0] < H_pos[0]:
                        T_pos = [H_pos[0] - 1, T_pos[1]]
                    # check if T is above H
                    if T_pos[0] > H_pos[0]:
                        T_pos = [H_pos[0] + 1, T_pos[1]]
                elif abs(T_pos[1] - H_pos[1]) > 1:  
                    #in different columns  
                    # check if T is left of H
                    if T_pos[1] < H_pos[1]:
                        T_pos = [T_pos[0], H_pos[1] - 1]
                    # check if T is right of H
                    if T_pos[1] > H_pos[1]:
                        T_pos = [T_pos[0], H_pos[1] + 1]
            # If not in same row/column and distance more than 1
            else:
                if abs(T_pos[0] - H_pos[0]) > 1 or abs(T_pos[1] - H_pos[1]) > 1:
                    # check if H is above
                    if T_pos[0] < H_pos[0]:
                        # check if H right:
                        if T_pos[1] < H_pos[1]:
                            T_pos = [T_pos[0] + 1, T_pos[1] + 1]
                        # check if H is left
                        if T_pos[1] > H_pos[1]:
                            T_pos = [T_pos[0] + 1, T_pos[1] - 1]
                    # check if H is below
                    elif T_pos[0] > H_pos[0]:  
                        # check if H right:
                        if T_pos[1] < H_pos[1]:
                            T_pos = [T_pos[0] - 1, T_pos[1] + 1]
                        # check if H is left
                        if T_pos[1] > H_pos[1]:
                            T_pos = [T_pos[0] - 1, T_pos[1] - 1]

            if T_pos not in visited:
                visited.append(T_pos)

    print(len(visited))