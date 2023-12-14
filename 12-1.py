f = open("12.txt").read().splitlines()

ans = 0

def check(springs, target):
    ans = 0
    if "?" in springs:
        ans += check(springs.replace("?", "#", 1), target)
        ans += check(springs.replace("?", ".", 1), target)
    else:
        workStreak = 0
        valid = True
        tempTarget = target[:]
        for i in springs:
            if i == "#":
                workStreak += 1
            elif i == "." and workStreak != 0:
                if len(tempTarget) == 0 or workStreak != tempTarget[0]:
                    valid = False
                    break
                else:
                    tempTarget = tempTarget[1:]
                    workStreak = 0
        if workStreak != 0:
            if len(tempTarget) == 0 or workStreak != tempTarget[0]:
                valid = False
            else:
                tempTarget = tempTarget[1:]
                workStreak = 0
        
        if valid and len(tempTarget) == 0:
            ans += 1
    return ans

ans = 0
for i in f:
    springs, target = i.split(" ")
    target = [int(i) for i in target.split(",")]    
    ans += check(springs, target)


print(ans)