f = open("4.txt").read().splitlines()



ans = 0
reps = [1 for _ in f]

for i,line in enumerate(f):
    info = line.replace("  ", " 0").split(": ")[-1]
    win, my = info.split(" | ")

    win = [int(i) for i in win.split(" ")]
    my = [int(i) for i in my.split(" ")]
    num = 0
    for j in win:
        if j in my:
            num += 1
    
    for j in range(num):
        if i + j + 1 == len(f):
            break
        reps[i + j + 1] += reps[i]

    
    ans += num * reps[i]



print(sum(reps))