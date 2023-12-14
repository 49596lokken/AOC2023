f= open("14.txt").read().splitlines()

def transpose(pattern):
    newPattern = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0])) ]
    return newPattern


def cycle(f):
    cols = []
    for col in range(len(f[0])):
        col = "".join(i[col] for i in f)
        col = col.split("#")
        cols.append("#".join("".join(sorted(c, reverse=True)) for c in col))

    f = ["".join(i) for i in transpose(cols)]

    

    rows = []
    for row in f:
        row = row.split("#")
        rows.append("#".join("".join(sorted(r, reverse=True)) for r in row))
    f = rows

    cols = []
    for col in range(len(f[0])):
        col = "".join(i[col] for i in f)
        col = col.split("#")
        cols.append("#".join("".join(sorted(c)) for c in col))
    f = ["".join(i) for i in transpose(cols)]


    rows = []
    for row in f:
        row = row.split("#")
        rows.append("#".join("".join(sorted(r)) for r in row))
   
    return rows

    

prevs = [f]
for i in range(1000000000):
    f = cycle(f)
    if f in prevs:
        cycleLength = len(prevs) - prevs.index(f)
        break
    prevs.append(f)


f = prevs[-((1000000000-i)%cycleLength)]


ans1 = []
for fi in (prevs[-cycleLength:]):
    ans = 0
    for i,line in enumerate(fi):
        ans += (len(line)-i)*line.count("O")
    ans1.append(ans)


print(ans1[(1000000000 - (len(prevs)-cycleLength)) % len(ans1)])




