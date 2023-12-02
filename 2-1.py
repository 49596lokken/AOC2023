f = open("2.txt").read().splitlines()



cols = {"red": 0, "blue":0, "green":0}
validsum = 0
for i, game in enumerate(f):
    game = game[game.index(":") + 2:]
    rounds = game.split("; ")
    valid = True
    for r in rounds:
        cols = {"red": 0, "blue":0, "green":0}
        t = r.split(", ")
        for p in t:
            print(p)

            n, col = p.split(" ")
            cols[col] += int(n)
            if not(cols["red"] <= 12 and cols["green"] <= 13 and cols["blue"] <= 14):
                valid = False
                print(cols)
                break
    print("Game Finished")
    if valid:
        validsum += i + 1

print(validsum)
