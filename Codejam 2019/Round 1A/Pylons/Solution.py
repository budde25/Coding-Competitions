from random import randint

def findPossibleMovesKnight(moves, bx, by):
    x, y = moves[-1].split(' ')
    x, y = int(x), int(y)
    knight = ['2 1', '2 -1', '-2 1', '-2 -1', '1 2', '1 -2', '-1 2', '-1 -2']
    possible = []
    for i in knight:
        kx, ky = i.split(' ')
        kx, ky = int(kx), int(ky)
        if (x + kx <= bx and x + kx >= 1 and y + ky <= by and y + ky >= 1):
            newMove = str(x + kx) + ' ' + str(y + ky)
            if (newMove not in moves):
                possible.append(newMove)
    return possible

def findPossibleMovesJump(moves, bx, by):
    x, y = moves[-1].split(' ')
    x, y = int(x), int(y)
    possible = []
    for i in range(1, bx + 1):
        for j in range(1, by + 1):
            if (i == x):
                slope = 0
            else:
                slope = (j - y) / (i - x)
            if (i != x and j != y and slope != 1 and slope != -1):
                newMove = str(i) + ' ' + str(j)
                if (newMove not in moves):
                    possible.append(newMove)
    return possible

def move(moves, bx, by):
    requiredMoves = bx * by
    while len(moves) != requiredMoves:   
        posKnight = findPossibleMovesKnight(moves, bx, by)
        while len(posKnight) != 0:
            moves.append(posKnight[randint(0, len(posKnight) - 1)])
            posKnight = findPossibleMovesKnight(moves, bx, by)
            if (bx == 2 and by == 5) or (by == 2 and bx == 5):
                break
        posJump = findPossibleMovesJump(moves, bx, by)
        if (len(posJump) == 0):
            return False
        moves.append(posJump[randint(0, len(posJump) -1)])
    return True

t = int(input())
for loop in range(1, t + 1):
    bx, by = [int(s) for s in input().split(" ")]
    if (bx == 2 and by == 2) or (bx == 3 and by == 2) or (bx == 2 and by == 3) or (bx == 4 and by == 2) or (bx == 2 and by == 4) or (bx == 3 and by == 3):
        print("Case #{}: IMPOSSIBLE".format(loop))
        continue
    moves = ['2 2']
    solution = move(moves, bx, by)
    while (not solution):
        moves = ['2 2']
        solution = move(moves, bx, by)

    print("Case #{}: POSSIBLE".format(loop))
    for i in moves:
        print(i)