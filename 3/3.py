with open('input.txt') as f:
    lines = f.readlines()
    rucksacks = [x.strip() for x in lines]

    def priority(letter):
        if letter.isupper():
            return ord(letter)-38
        else:
            return ord(letter)-96
   
    tot_prio = 0

    for rucksack in rucksacks:
        middle = (len(rucksack)/2)
        first = list(rucksack[0:middle])
        second = list(rucksack[middle:])

        for letter in first:
            if letter in second:
                tot_prio+= priority(letter)
                break

    print(tot_prio)