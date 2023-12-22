#Drunk on bus is not the vibe

f = open("16.txt").read().splitlines()


i,j = 0,0

dir = (0,1)

energised = [[[]for j in i] for i in f]


def energise(i,j, dir):
    while True:
        if dir in energised[i][j]:
            return

        energised[i][j].append(dir)

        if f[i][j] == "\\":
            dir = dir[::-1]
        
        elif f[i][j] == "/":
            dir = tuple(-i for i in dir[::-1])
        
        elif f[i][j] == "|":
            if dir[0] == 0:
                if i-1 >= 0:
                    energise(i-1, j, (-1, 0)) 
                dir = (1, 0)
        
        elif f[i][j] == "-":
            if dir[1] == 0:
                if j-1 >= 0:
                    energise(i, j-1, (0, -1))
                dir = (0,1)

        if i + dir[0] >= 0 and i + dir[0] < len(energised) and j + dir[1] >= 0 and j+dir[1] < len(energised[0]):
            i,j = i + dir[0], j+dir[1]
    

energise(i, j, dir)

ans = ""
for i in energised:
    for j in i:
        if j:
            ans += "#"
        else:
            ans += "."
    ans += "\n"

print(ans.count("#"))
