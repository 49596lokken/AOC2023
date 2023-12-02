f = open("2.txt").read().splitlines()



cols = {"red": 0, "blue":0, "green":0}
powerSum = 0
for i, game in enumerate(f):
    game = game[game.index(":") + 2:]
    rounds = game.split("; ")
    maxCols = {i:0 for i in cols}
    for r in rounds:
        cols = {"red": 0, "blue":0, "green":0}
        t = r.split(", ")
        for p in t:
            print(p)

            n, col = p.split(" ")
            cols[col] += int(n)
        for col in cols:
            if cols[col] > maxCols[col]:
                maxCols[col] = cols[col]
    powerSum += maxCols["red"] * maxCols["green"] * maxCols["blue"]

print(powerSum)
