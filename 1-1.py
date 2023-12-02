f = open("1.txt").readlines()
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

calval = []
for line in f:
    val = 0
    for i in line:
        if i.isnumeric():
            val += int(i)*10
            break
    for j in line[::-1]:
        if j.isnumeric():
            val += int(j)
            break

    calval.append(int(val))

print(sum(calval))