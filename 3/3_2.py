with open('input.txt') as f:
    lines = f.readlines()
    rucksacks = [x.strip() for x in lines]

    def priority(letter):
        if letter.isupper():
            return ord(letter)-38
        else:
            return ord(letter)-96
   
    tot_prio = 0
    i = 0;
    while i <= len(rucksacks)-2:
        print(i)
        first = list(rucksacks[i])
        second = list(rucksacks[i+1])
        third = list(rucksacks[i+2])
        i+=3
        for letter in first:
            if letter in second and letter in third:
                print(letter)
                tot_prio+= priority(letter)
                break

    print(tot_prio)