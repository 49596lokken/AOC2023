f = open("7.txt").readlines()


hands = [i.split(" ")[0] for i in f]
bids = [int(i.split(" ")[1]) for i in f]



rankings = [i+1 for i in range(len(hands))]

no_j = [str(i) for i in range(2,10)]
no_j.extend(["T", "Q", "K", "A"])

cards = ["J"] + no_j

def cmp(h1, h2):
    #True if h1 better
    h1_j, h2_j = False, False
    h1_old, h2_old = h1,h2
    
    if "J" in h1:
        best = h1.replace("J", "2")
        for c in no_j[1:]:
            new = h1.replace("J", c)
            if cmp(new, best):
                best = new
        h1 = best
    
    if "J" in h2:
        best = h2.replace("J", "2")
        for c in no_j[1:]:
            new = h2.replace("J", c)
            if cmp(new, best):
                best = new
        h2 = best
     
    

    counts1 = sorted([h1.count(i) for i in h1])
    counts2 = sorted([h2.count(i) for i in h2])

    if counts1 == [5,5,5,5,5]:
        if counts2 == [5,5,5,5,5]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True
    

    if counts2 == [5,5,5,5,5]:
        return False
    
    if counts1 == [1,4,4,4,4]:
        if counts2 == [1,4,4,4,4]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True

    if counts2 == [1,4,4,4,4]:
        return False
    
    if counts1 == [2,2,3,3,3]:
        if counts2 == [2,2,3,3,3]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True

    if counts2 == [2,2,3,3,3]:
        return False
    
    if counts1 == [1,1,3,3,3]:
        if counts2 == [1,1,3,3,3]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True

    if counts2 == [1,1,3,3,3]:
        return False
    
    if counts1 == [1,2,2,2,2]:
        if counts2 == [1,2,2,2,2]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True

    if counts2 == [1,2,2,2,2]:
        return False
    
    if counts1 == [1,1,1,2,2]:
        if counts2 == [1,1,1,2,2]:
            for i in range(5):
                if h1_old[i] != h2_old[i]:
                    return cards.index(h1_old[i]) > cards.index(h2_old[i])
        return True

    if counts2 == [1,1,1,2,2]:
        return False
    
    
    for i in range(5):
       if h1_old[i] != h2_old[i]:
            return cards.index(h1_old[i]) > cards.index(h2_old[i])

print(cmp("JJJJJ", "J7777"))
print(cmp("J7777", "JJJJJ"))

listSorted = False
passes = 0
while not listSorted:
    listSorted = True
    for i in range(len(hands)-1):
        if cmp(hands[i], hands[i+1]):
            hands[i], hands[i+1] = hands[i+1], hands[i]
            bids[i], bids[i+1] = bids[i+1], bids[i]
            listSorted = False
    passes += 1

out = 0
for i in range(len(hands)):
    out += bids[i] * (i+1)

    print(i+1, hands[i], bids[i])

for i in range(len(hands)):
    for j in range(i+1, len(hands)):
        if cmp(hands[i], hands[j]):
            print(i, j)

print(out)
