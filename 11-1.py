f = open("11.txt").read().splitlines()

f = [list(i) for i in f]

newFile = [[j for j in i] for i in f]
badRows = 0
for i, line in enumerate(f):
    if "#" not in line:
        newFile.insert(i + badRows, line)
        badRows += 1



print("Now cols")
badCols = 0
for j in range(len(f[i])):
    hasGalaxy = False
    for line in f:
        if line[j] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        for i in range(len(newFile)):
            newFile[i].insert(j+badCols, ".")
        badCols += 1




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
        ans += abs(a-c) + abs(b-d)
        print(i+1, j+1, abs(a-c) + abs(b-d))

print(ans)

