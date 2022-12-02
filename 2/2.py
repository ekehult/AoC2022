#rock = 1 p, paper = 2p, scissor = 3p
#rock > scissor, scissor > paper, paper > rock
#win = 6p, draw = 3p, loss = 0p
#A,X = rock, B,Y = paper, C,Z = scissor

def game(opponent, mine):
    #win
    if opponent == 'paper' and mine == 'scissor':
        return 6
    if opponent == 'rock' and mine == 'paper':
        return 6
    if opponent == 'scissor' and mine == 'rock':
        return 6
    #draw
    if opponent == mine:
        return 3
    else:
        return 0

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    count = 0
    for line in lines:
        if line[0] == 'B':
            opp = 'paper'
        elif line[0] == 'A':
            opp = 'rock'
        elif line[0] == 'C':
            opp = 'scissor'
        if line[2] == 'Y':
            mine = 'paper'
            count+=2
        elif line[2] == 'X': 
            mine = 'rock'
            count+=1
        elif line[2] == 'Z':
            mine = 'scissor'
            count+=3
        count+= game(opp, mine)
        
    print(count)