import sys

score = 0
pos = 0
turn_done = 0
turn = 0
tmp = []
scores = sys.argv[1]

def changeToInt(pin):

    if pin == "X":
        return 10
    elif pin == "/":
        return 10
    elif pin == "-":
        return 0
    else:
        return int(pin);

def checkStrikes(pin1, pin2):
    if pin2 == "/":
        return 20
    else:
        return 10 + changeToInt(pin1) + changeToInt(pin2);


for s in scores:

    if turn == 10:
        break
    elif s == "X":
        score= score + checkStrikes(scores[pos+1],scores[pos+2])
        turn_done = 0
        turn = turn + 1
    elif s == "/":
        score = score + 10 + changeToInt(scores[pos+1])
        turn_done = 0
        turn = turn + 1
    else:
        if turn_done == 0:
            tmp = changeToInt(s)
            turn_done = turn_done +1
        else:
            score = score +tmp + changeToInt(s)
            turn_done = 0
            turn = turn + 1
    pos = pos + 1

print(score)
