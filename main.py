# Rock = 1 Paper = 2 Scissors = 3
# Win = 6, Even = 3, Lost = 0
# X lose, Y draw, Z win

import re

oponent_d = {"A": '1',  "B": '2',  "C": '3'}
me_d = {"X": 'L',  "Y": 'D',  "Z": 'W'}

def getLineOutput2(oponent, me):
    if oponent == '1':  # Rock
        if me == 'W':  # paper
            return 2+6
        if me == 'D': #rock
            return 3+1
        if me == 'L': #scissor
            return 3
    if oponent == '2':  # paper
        if me == 'W':  # scissor
            return 3+6
        if me == 'D': #paper
            return 3+2
        if me == 'L': #rock
            return 1
    if oponent == '3':  # scissors
        if me == 'W':  # rock
            return 1+6
        if me == 'D': #scissors
            return 3+3
        if me == 'L': #paper
            return 2

    print("sakjsa")



def getLineOutput(oponent, me):
    if me == '1': #Rock
        if oponent == '1': #Rock
            return 1+3  #even
        elif oponent == "2": #paper
            return 1   #lost
        elif oponent == "3": #scissors
            return 1+6  #won
    elif me == '2': #Paper
        if oponent == '1': #Rock
            return 2+6  #win
        elif oponent == "2": #paper
            return 2+3   #even
        elif oponent == "3": #scissors
            return 2  #lost
    elif me == '3': #Scissors
        if oponent == '1': #Rock
            return 3  #lost
        elif oponent == "2": #paper
            return 3+6   #win
        elif oponent == "3": #scissors
            return 3+3  #even

total = 0
with open('input.txt', 'r') as reader:
    line = reader.readline()

    while line != '':
        res = re.split(' |\n', line)
        total += getLineOutput2(oponent_d[res[0]], me_d[res[1]])
        print(getLineOutput2(oponent_d[res[0]], me_d[res[1]]))
        line = reader.readline()

print(total)