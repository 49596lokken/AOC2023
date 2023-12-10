f = open("10.txt").readlines()




for i,line in enumerate(f):
    if "S" in line:
        start = (i,line.index("S"))

def surrounding(i,j):
    out = []
    c = f[i][j]
    
    if c == "|":
        if i - 1 >= 0:
            out.append((i-1,j))
        if i + 1 < len(f):
            out.append((i+1, j))
    elif c == "-":
        if j - 1 >= 0:
            out.append((i,j-1))
        if j + 1 < len(f[i]):
            out.append((i, j+1))
    elif c == "L":
        if i - 1 >= 0:
            out.append((i-1,j))
        if j + 1 < len(f[i]):
            out.append((i, j+1))
    elif c == "J":
        if i - 1 >= 0:
            out.append((i-1,j))
        if j - 1 >= 0:
            out.append((i, j-1))
    elif c == "7":
        if i + 1 < len(f):
            out.append((i+1,j))
        if j - 1 >= 0:
            out.append((i, j-1))
    elif c == "F":
        if i + 1 < len(f):
            out.append((i+1,j))
        if j + 1 < len(f[i]):
            out.append((i, j+1))
    elif c == "S":

        for a in range(-1,2):
            if a + i < 0 or a + i >= len(f):
                continue
            out.append((i+a,j))

        for b in range(-1,2):
            if b + j < 0 or b + j >= len(f[i]):
                continue
            out.append((i,j+b))
        out.remove((i,j))
    return out

distances = [[-1 for i in line] for line in f]

def traverse(i,j, visited = []):
    visited.append((i,j))
    finished = False
    currentLayer = [(i,j)]
    layer = 1
    while not finished:
        newLayer = []
        for pos in currentLayer:
            i,j = pos
            for newPos in surrounding(i,j):
                
                a,b = newPos
                c = f[a][b]
                if (a,b) in visited:
                    continue
                if c == "|":
                    if a!=i and b==j:
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer

                elif c == "-":
                    if b != j and a==i:
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer
                elif c == "L":
                    if (a == i+1 and b==j) or (a==i and b == j-1):
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer
                elif c == "J":
                    if (a == i+1 and b==j) or (a==i and b == j+1):
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer
                elif c == "7":
                    if (a == i-1 and b==j) or (a==i and b == j+1):
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer
                elif c == "F":
                    if (a == i-1 and b==j) or (a==i and b == j-1):
                        visited.append((a,b))
                        newLayer.append((a,b))
                        if distances[a][b] == -1:
                            distances[a][b] = layer
                elif c == "S":
                    visited.append((a,b))
                    newLayer.append((a,b))
                    if distances[a][b] == -1:
                            distances[a][b] = layer
                max(1,2)
        layer += 1
        if len(newLayer) == 0:
            return visited + currentLayer
        currentLayer = newLayer[:]


path = traverse(start[0], start[1])


waiting = False
down = False
inside = 0
ans = 0

for i, row in enumerate(f):
    for j, c  in enumerate(row):
        if c == "S":
            c = "|" #Basically just manually verified that the given input starts with a vertical pipe. I know its bad but idc

        if (i,j) not in path:
            ans += inside
            
        if (i,j) in path:
            if c == "|":
                inside = 1-inside
            if c in "FLJ7":
                if waiting:
                    if (c in "F7") ^ down:
                        inside = 1-inside
                else:
                    down = c in "F7"
                waiting = not(waiting)

print(ans)

