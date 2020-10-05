
from collections import Counter
# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    size = int(input())
    matrix = []
    for j in range(size):
        matrix.append(input().split(" "))

    sum = 0
    for a in range(len(matrix)):
       sum += int(matrix[a][a])

    r, c = 0,0
    for a in matrix:
        arr = []
        for b in a:
            arr.append(int(b))
        
        dic = dict(Counter(arr))
        add = 0
        for k in dic.values():
            if k > 1:
                add += k
        r = max(r, add)

    for a in range(size):
        arr = []
        for b in range(size):
            arr.append(int(matrix[b][a]))
        dic = dict(Counter(arr))
        add = 0
        for k in dic.values():
            if k > 1:
                add += k
        c = max(r, add)

    print("Case #{}: {} {} {}".format(i, sum, r, c))
    # check out .format's specification for more formatting options
      