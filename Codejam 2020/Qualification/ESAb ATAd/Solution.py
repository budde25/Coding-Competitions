t, b = input().split()
t, b = int(t), int(b)

def getPoss(curr):
    poss = []
    current = curr[:]
    reverse = curr[::-1]
    flip = curr[:]

    for i in range(len(flip)):
        if flip[i] == '0':
            flip[i] = '1'
        elif flip[i] == '1':
            flip[i] = '0'
        else:
            continue

    flipreverse = flip[::-1]

    poss.append(current)
    poss.append(reverse)
    poss.append(flip)
    poss.append(flipreverse)
    return poss

def check20(poss):
    print(19)
    ans19 = input()
    print(20)
    ans20 = input()
    new = []
    for p in poss:
        if ans19 == p[18]:
            new.append(p)
        if ans20 == p[19]:
            new.append(p)
    poss = new
    


def cases():
    for case in range(t):
        arr = [None] * b
        possible = []
        for i in range(1,11):
            print(i)
            arr[i - 1] = input()
        if(b == 10):
            possible = getPoss(arr)
            for i in range(1,10):
                print(i)
                num = input()
                new = []
                for p in possible:
                    if p[i - 1] == num:
                        new.append(p)
                possible = new
                if (len(possible) == 1):
                    break
            if len(possible) > 0:
                print(''.join(possible[0]))
            else:
                print("1001")
            if input() == 'N':
                return
            else:
                continue
        
        if(b != 10):
            possible = getPoss(arr)
            depth = 11
            while(True):
                
                # pick two spots to check and continue going
                spot1 = depth - 1
                spot2 = (depth / 2) + 2 # try not to hit the middle
                print(spot1)
                ans1 = input()
                print(spot2)
                ans2 = input()
                new = []
                for p in possible:
                    if possible[spot1 - 1] == ans1: 
                        new.append(p)
                    if possible[spot2 - 1] == ans2: 
                        new.append(p)
                possible = new
                for i in range(depth, depth+8):
                    print(i)
                    res = input()
                    for p in possible:
                        p[i - 1] = res
                new = []
                for p in possible:
                    new += getPoss(p)
                possible = new
                depth+=8
                if (b == 20):
                    check20(possible)
                    break
        

cases()