with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    overlaps = 0
    for line in lines:
        first = line.split(',')[0].split('-')
        second = line.split(',')[1].split('-')
        if int(first[0]) in range(int(second[0]), int(second[1])+1) and int(first[1]) in range(int(second[0]), int(second[1])+1):
            overlaps+=1
        elif int(second[0]) in range(int(first[0]), int(first[1])+1) and int(second[1]) in range(int(first[0]), int(first[1])+1):
            overlaps+=1
    print(overlaps)
        