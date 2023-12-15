f= open("15.txt").read().splitlines()


def h(a):
    current = 0
    for i in a:
        current += ord(i)
        current *= 17
        current %= 256
    return current

i = f[0].split(",")

boxes = [dict() for _ in range(256)]

for j in i:
    if "-" in j:
        lab = j[:-1]
        boxNum = h(lab)
        if lab in boxes[boxNum]:
            del boxes[boxNum][lab]
    else:
        lab, num = j.split("=")
        boxNum = h(lab)
        boxes[boxNum][lab] = int(num)

ans = 0
for i in range(len(boxes)):
    for j, lab in enumerate(boxes[i]):
        ans += (i+1) * (j+1) * boxes[i][lab]

print(ans)
