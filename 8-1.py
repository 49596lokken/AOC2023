f = open("8.txt").read().splitlines()

instructions = f[0]

maps = {i[0:3]: {"L":i[7:10], "R":i[12:15]} for i in f[2:]}

loc = "AAA"
steps = 0
found = False
while not found:
    for instruction in instructions:
        steps += 1
        loc = maps[loc][instruction]
        if loc == "ZZZ":
            print(steps)
            found = True
            break