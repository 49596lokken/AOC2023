patterns = open("13.txt").read().split("\n\n")

patterns = [[[i for i in j] for j in k.split("\n")] for k in patterns]


def transpose(pattern):
    newPattern = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0])) ]
    return newPattern



ans = 0

for ind, pattern in enumerate(patterns):
    
    val = 0
    for i in range(len(pattern)-1):
        length = min(i + 1, len(pattern)-i-1)
        p1 = pattern[i::-1][:length]
        p2 = pattern[i+1:][:length]
        if p1 == p2:
            refline = (i+1, 100)
            break
    
    pattern = transpose(pattern)
    for i in range(len(pattern)-1):
        length = min(i + 1, len(pattern)-i-1)
        p1 = pattern[i::-1][:length]
        p2 = pattern[i+1:][:length]
        if p1 == p2:
            if val != 0:
                print(ind)
            refline = (i+1, 1)
            break

    pattern = transpose(pattern)
    newrefline = (-1, -1)
    for a in range(len(pattern)):
        for b in range(len(pattern[a])):
            if pattern[a][b] == ".":
                pattern[a][b] = "#"
            else:
                pattern[a][b] = "."
            val = 0
            for i in range(len(pattern)-1):
                length = min(i + 1, len(pattern)-i-1)
                p1 = pattern[i::-1][:length]
                p2 = pattern[i+1:][:length]
                if p1 == p2:
                    if (i+1, 100) != refline:
                        newrefline = (i+1, 100)
                        #print(ind, 100, newrefline)
                        break
            
            pattern = transpose(pattern)
            for i in range(len(pattern)-1):
                length = min(i + 1, len(pattern)-i-1)
                p1 = pattern[i::-1][:length]
                p2 = pattern[i+1:][:length]
                if p1 == p2:
                    if (i+1,1) != refline:
                        newrefline = (i+1, 1)
                        #print(ind, 1, newrefline)
                        break
            

            pattern = transpose(pattern)
            if pattern[a][b] == ".":
                pattern[a][b] = "#"
            else:
                pattern[a][b] = "."
    if newrefline == (-1, -1):
        print(ind)
        print("\n".join("".join(j for j in i) for i in pattern))
    if newrefline != refline:
        val += newrefline[0] * newrefline[1]
    ans += val

print(ans)
