f = open("11.txt").read().splitlines()

f = [list(i) for i in f]

newFile = [[j for j in i] for i in f]
badRows = []
for i, line in enumerate(f):
    if "#" not in line:
        badRows.append(i)



print("Now cols")
badCols = []
for j in range(len(f[i])):
    hasGalaxy = False
    for line in f:
        if line[j] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        badCols.append(j)




f = newFile[:]
galaxies = []

for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "#":
            galaxies.append((i,j))




ans = 0
for i in range(len(galaxies)-1):
    for j in range(i, len(galaxies)):
        a,b = galaxies[i]
        c,d = galaxies[j]
        if a > c:
            a,c=c,a
        if b > d:
            b,d = d,b
        
        offset = 0
        for row in range(a,c):
            if row in badRows:
                offset += 1000000-1
        
        for col in range(b,d):
            if col in badCols:
                offset += 1000000-1
        
        ans += abs(a-c) + abs(b-d) + offset


print(ans)

