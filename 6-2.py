f = open("6.txt").read().splitlines()



times = [int(i) for i in f[0].removeprefix("Time: ").strip().split(" ") if i != ""]
distance = [int(i) for i in f[1].removeprefix("Distance: ").strip().split(" ") if i != ""]

prod = ["", ""]
for i in range(len(times)):
    prod[0] += str(times[i])
    prod[1] += str(distance[i])

times = [int(prod[0])]
distance = [int(prod[1])]

ans = 1

print(int((times[0] + (times[0]**2 - 4*distance[0])**0.5)/2) - int((times[0] - (times[0]**2 - 4*distance[0])**0.5)/2))

