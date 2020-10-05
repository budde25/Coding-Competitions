t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    unstr = input()

    #get max val
    top = 0
    for j in unstr:
        if int(j) > top:
            top = int(j)
    

    for num in range(1, top + 1):
        newstr = ""
        openl = True
        for j in unstr:
            if (openl and (j == str(num))):
                newstr += '('
                openl = False
            if ((not openl) and (j < str(num))):
                newstr += ')'
                openl = True
            newstr += j
            
        if (not openl):
                newstr += ')'
        unstr = newstr

    print("Case #{}: {}".format(i, unstr))