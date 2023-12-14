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
            val += 100*(i+1)
            break
    
    pattern = transpose(pattern)
    for i in range(len(pattern)-1):
        length = min(i + 1, len(pattern)-i-1)
        p1 = pattern[i::-1][:length]
        p2 = pattern[i+1:][:length]
        if p1 == p2:
            if val != 0:
                print(ind)
            val += (i+1)
            break

    if val == 0:
        print(ind, 0)
    
    ans += val

print(ans)
