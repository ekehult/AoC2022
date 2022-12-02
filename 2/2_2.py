#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
#rock = 1 p, paper = 2p, scissor = 3p
#rock > scissor, scissor > paper, paper > rock
#win = 6p, draw = 3p, loss = 0p
#A = rock, B = paper, C  = scissor

def game(opponent, result):
    #win
    if result == 'win':
        if opponent == 'rock':
            #paper
            return 8
        if opponent == 'scissor':
            #rock
            return 7
        if opponent == 'paper':
            #scissor
            return 9
    #draw
    if result == 'draw':
        if opponent == 'rock':
            return 4
        if opponent == 'scissor':
            return 6
        if opponent == 'paper':
            return 5
    #loss
    else:
        if opponent == 'rock':
            #scissor
            return 3
        if opponent == 'scissor':
            #paper
            return 2
        if opponent == 'paper':
            #rock
            return 1

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
            result = 'draw'
        elif line[2] == 'X': 
            result = 'lose'
        elif line[2] == 'Z':
            result = 'win'
        count+= game(opp, result)
        
    print(count)