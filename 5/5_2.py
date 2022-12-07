
with open('input.txt') as f:
    lines = f.readlines()
    index = lines.index('\n')
    stacks = lines[0:index-1]
    instructions = lines[index+1:]

    num_stacks = int(max(lines[index-1]))
    all_stacks = []
    
    for i in range(len(stacks[0])):
        lis = []
        for stack in stacks:
            if stack[i].isalpha():
                lis.append(stack[i])
        if len(lis) > 0:
            all_stacks.append(lis)

    for instruction in instructions:
        split_instruct = instruction.split(' ')
        amount = int(split_instruct[1])
        from_stack = int(split_instruct[3])-1
        to_stack = int(split_instruct[5])-1
        move = []
        for i in reversed(range(amount)):
            move = all_stacks[from_stack].pop(i)
            all_stacks[to_stack].insert(0, move)
    
    for stack in all_stacks:
        print(stack[0])