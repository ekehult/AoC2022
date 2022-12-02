
with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    max_cal = 0
    cals = 0
    for line in lines:
        if len(line) > 0:
            cals+=int(line)
        else:
            if cals > max_cal:
                max_cal = cals
            cals = 0
    if cals > max_cal:
                max_cal = cals
    print(max_cal)