def removeNoRhyme(words):
    loopWords = words.copy()
    for i in loopWords:
        count = 0
        for j in words:
            if i[:1] == j[:1]:
                count = count + 1
        if count == 1:
            words.remove(i)

def getBestMatch(words, exclude):
    if len(words) == 1 or words[0][0] != words[1][0]:
        words.pop(0)
        return False
    count = 0
    x = ''
    for i in range(len(words)):
        prevX = x
        x = ''
        prevCount = count
        count = 0
        if i + 1 == len(words):
            words.pop(i)
            words.pop(i - 1)
            if prevX not in exclude:
                exclude.append(prevX)
                return True
            else:
                return False
        for j in range(min(len(words[i]), len(words[i + 1]))):
            if words[i][j] == words[i + 1][j]:
                count = count + 1
                x = x + words[i][j]
            else:
                if prevCount >= count and prevCount != 0:
                    words.pop(i)
                    words.pop(i - 1)
                    if prevX not in exclude:
                        exclude.append(prevX)
                        return True
                    else:
                        return False
                else:
                    break
        
            


t = int(input())
for loop in range(1, t + 1):
    numRhymes = 0
    numWords = int(input())
    words = []
    exclude= []
    for i in range(numWords):
        words.append(input()[::-1])
    words.sort()
    removeNoRhyme(words)
    while len(words) != 0:
        if getBestMatch(words, exclude):
            numRhymes = numRhymes + 2
    print("Case #{}: {}".format(loop, numRhymes))