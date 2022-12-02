
with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    tot_cals = []
    cals = 0
    for line in lines:
        if len(line) > 0:
            cals+=int(line)
        else:
            tot_cals.append(cals)
            cals = 0

    tot_cals.append(cals)

    tot_cals.sort()
 
    print(tot_cals[-1]+tot_cals[-2]+tot_cals[-3])
    