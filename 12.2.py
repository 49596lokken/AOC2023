f = open("12.txt").read().splitlines()

ans = 0

def check(springs, target, prev="."):
    ans = 0
    if len(target) == 0:
        return "#" not in springs
    if len(springs) == 0:
        return 0
    if springs[0] == "#":
        if len(target) == 0 or len(springs) < target[0] or "." in springs[:target[0]] or (len(springs) != target[0] and springs[target[0]] == "#"):
            return 0
        return check(springs[target[0]+1:], target[1:])
    elif springs[0] == ".":
        return check(springs[1:], target)
    else:
        if "#" not in springs and "." not in springs:
            
        ans += check(springs.replace("?", "#", 1), target)
        if len(springs) >= sum(target) + len(target):
            ans += check(springs.replace("?", ".", 1), target)
    return ans

print(check("?###????????", [3,2,1]))

ans = 0
for i,line in enumerate(f):
    springs, target = line.split(" ")
    target = [int(i) for i in target.split(",")]    
    
    target = target * 5
    springs = (springs + "?")*4 + springs

    
    c = check(springs, target)

    print(c)

    ans += c
    #print(i/len(f))

print(ans)