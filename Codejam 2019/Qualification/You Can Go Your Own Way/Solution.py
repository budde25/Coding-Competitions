t = int(input())
for i in range(1, t + 1):
    n, m = input(), input()
    for j in range(len(m)):
        if m[j] == 'S':
            m = m[:j] + 'E' + m[j+1:]
        else:
            m = m[:j] + 'S' + m[j+1:]
    print("Case #{}: {}".format(i, m))