f = open("6.txt").read().splitlines()



times = [int(i) for i in f[0].removeprefix("Time: ").strip().split(" ") if i != ""]
distance = [int(i) for i in f[1].removeprefix("Distance: ").strip().split(" ") if i != ""]



ans = 1
for i,time in enumerate(times):
    numWins = 0
    for j in range(time):
        if j * (times[i] - j) > distance[i]:
            numWins += 1
    ans *= numWins

print(ans)