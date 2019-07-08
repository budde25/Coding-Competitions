import math


def findPrimes(limit):
    sqrt = math.ceil(math.sqrt(limit))

    primes = []
    for i in range(math.ceil(limit / 2)):
        primes.append(i * 2 + 1)
    primes.remove(1)
    primes.insert(0, 2)

    for i in range(len(primes) - 1, 0, -1):
        for j in range(2, sqrt):
            if primes[i] % j == 0 and primes[i] != j:
                primes.pop(i)
                break

    return primes


t = int(input())
for loop in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    cipherText = input().split(" ")
    primes = findPrimes(n)

    possible = []
    for i in cipherText:
        for j in primes:
            if int(i) % j == 0:
                possible.append([j, int(int(i) / j)])
                break

    cipher = []
    for i in range(len(possible) - 1):
        if possible[i][0] in possible[i + 1]:
            cipher.append(possible[i][0])
        else:
            cipher.append(possible[i][1])
    if possible[0][0] == cipher[0]:
        cipher.insert(0, possible[0][1])
    else:
        cipher.insert(0, possible[0][0])
    if possible[-1][0] == cipher[-1]:
        cipher.append(possible[-1][1])
    else:
        cipher.append(possible[-1][0])

    usedPrimes = list(dict.fromkeys(cipher))
    usedPrimes.sort()

    alphabet = [['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], ['I'], ['J'], ['K'], ['L'], [
        'M'], ['N'], ['O'], ['P'], ['Q'], ['R'], ['S'], ['T'], ['U'], ['V'], ['W'], ['X'], ['Y'], ['Z']]
    for i in range(len(alphabet)):
        alphabet[i].append(usedPrimes[i])

    answer = ''
    for i in cipher:
        for j in range(len(alphabet)):
            if int(i) in alphabet[j]:
                answer = answer + alphabet[j][0]

    print("Case #{}: {}".format(loop, answer))
