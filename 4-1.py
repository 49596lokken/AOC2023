f = open("4.txt").read().splitlines()




ans = 0

for i,line in enumerate(f):
    info = line.replace("  ", " 0").split(": ")[-1]
    win, my = info.split(" | ")
    print(win, my)

    win = [int(i) for i in win.split(" ")]
    my = [int(i) for i in my.split(" ")]
    num = 0
    for i in win:
        if i in my:
            num += 1
            print(i)

    if num != 0:
        ans += 2**(num-1)
    print(num)
print(ans)