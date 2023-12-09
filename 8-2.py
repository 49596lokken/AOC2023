f = open("8.txt").read().splitlines()

instructions = f[0]

maps = {i[0:3]: {"L":i[7:10], "R":i[12:15]} for i in f[2:]}

loc = "AAA"

found = False

minSteps = 0

stepArray = []

for map in maps:
    if map[2] == "A":
        loc = map
        steps = 0
        found = False
        while not found:
            for instruction in instructions:
                steps += 1
                loc = maps[loc][instruction]
                if loc[2] == "Z":
                    found = True
                    break
        stepArray.append(steps)

def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

def lcm(ns):
    if len(ns) == 2:
        a,b = ns
        return a * b // gcd(a,b)
        
    
    return lcm([lcm([ns[0], ns[1]])] + ns[2:])


print(lcm(stepArray))