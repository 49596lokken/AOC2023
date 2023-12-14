f= open("14.txt").read().splitlines()

def transpose(pattern):
    newPattern = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0])) ]
    return newPattern

cols = []
for col in range(len(f[0])):
    col = "".join(i[col] for i in f)
    cubeIndices = [i for i in range(len(col)) if col[i] == "#"] 
    col = col.split("#")
    cols.append("#".join("".join(sorted(c, reverse=True)) for c in col))

f = transpose(cols)

ans = 0
for i,line in enumerate(f):
    ans += (len(line)-i)*line.count("O")
print(ans)