t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    acts = int(input())
    JF, CF = 0, 0
    sch = [None] * acts
    times = []
    for act in range(acts):
        start, end = input().split(" ")
        times.append([int(start), int(end), act])

    times = sorted(times, key=lambda x: x[0])
    print(times)
    for time in times:
        if (time[0] >= JF):
            JF = time[1]
            sch[time[2]] = "C"
        elif (time[0] >= CF):
            CF = time[1]
            sch[time[2]] = "J"
        else:
            sch = None
            break
    
    if sch == None:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, " ".join(sch)))