f = open("1.txt").readlines()


numbers = ["\u1235", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
revnumbers = [n[::-1] for n in numbers]

calval = []
for line in f:
    val = 0
    indices = [line.index(n) if n in line else -1 for n in numbers]
    for i in range(len(line)):
        if i in indices :
            val += indices.index(i)*10
            break
        if line[i].isnumeric():
            val += int(line[i])*10
            break
    line = line[::-1]
    indices = [line.index(n) if n in line else -1 for n in revnumbers]
    #print(val, indices, line)
    for j in range(len(line)):
        if j in indices:
            val += indices.index(j)
            break
        if line[j].isnumeric():
            val += int(line[j])
            break

    print(f"{line[::-1]}, {val}")

    calval.append(int(val))

print(sum(calval))