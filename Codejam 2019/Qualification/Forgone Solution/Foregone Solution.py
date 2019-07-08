t = int(input())
for i in range(1, t + 1):
    n = input()
    m = ""
    for j in range(len(n)):
        m = m + "0"
    if "4" in n:
        for j in range(len(n)):
            if(n[j] == "4"):
                n = n[:j] + "3" + n[j+1:]
                m = m[:j] + "1" + m[j+1:]
        print("Case #{}: {} {}".format(i, int(n), int(m)))
    else:
        print("Case #{}: {} {}".format(i, int(n), 0))