f= open("15.txt").read().splitlines()


def h(a):
    current = 0
    for i in a:
        current += ord(i)
        current *= 17
        current %= 256
    return current

i = f[0].split(",")

ans = 0
for j in i:
    ans += h(j)

print(ans)
