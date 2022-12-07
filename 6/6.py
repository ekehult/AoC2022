with open('input.txt') as f:
    lines = f.readlines()
    
    temp = []
    for i in range(3):
        temp.append(lines[0][i])

    def duplicate(list):
        for letter in list:
            if list.count(letter) > 1:
                return True
        return False

    i = 4
    for letter in lines[0][3:]:
        if letter not in temp:
            if not duplicate(temp):
                print(i)
                break
            else:
                temp.pop(0)
                temp.append(letter)
        else: 
            temp.pop(0)
            temp.append(letter)
        i+=1
