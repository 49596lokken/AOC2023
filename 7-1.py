f = open("7.txt").readlines()



hands = [i.split(" ")[0] for i in f]
bids = [int(i.split(" ")[1]) for i in f]



rankings = [i+1 for i in range(len(hands))]

cards = [str(i) for i in range(2,10)]
cards.extend(["T", "J", "Q", "K", "A"])



def cmp(h1, h2):
    #True if h1 better
    


    counts1 = sorted([h1.count(i) for i in h1])
    counts2 = sorted([h2.count(i) for i in h2])

    if counts1 == [5,5,5,5,5]:
        if counts2 == [5,5,5,5,5]:
            return cards.index(h1[0]) > cards.index(h2[0])
        return True
    

    if counts2 == [5,5,5,5,5]:
        return False
    
    if counts1 == [1,4,4,4,4]:
        if counts2 == [1,4,4,4,4]:
            for i in range(5):
                if h1[i] != h2[i]:
                    return cards.index(h1[i]) > cards.index(h2[i])
        return True

    if counts2 == [1,4,4,4,4]:
        return False
    
    if counts1 == [2,2,3,3,3]:
        if counts2 == [2,2,3,3,3]:
            for i in range(5):
                if h1[i] != h2[i]:
                    return cards.index(h1[i]) > cards.index(h2[i])
        return True

    if counts2 == [2,2,3,3,3]:
        return False
    
    if counts1 == [1,1,3,3,3]:
        if counts2 == [1,1,3,3,3]:
            for i in range(5):
                if h1[i] != h2[i]:
                    return cards.index(h1[i]) > cards.index(h2[i])
        return True

    if counts2 == [1,1,3,3,3]:
        return False
    
    if counts1 == [1,2,2,2,2]:
        if counts2 == [1,2,2,2,2]:
            for i in range(5):
                if h1[i] != h2[i]:
                    return cards.index(h1[i]) > cards.index(h2[i])
        return True

    if counts2 == [1,2,2,2,2]:
        return False
    
    if counts1 == [1,1,1,2,2]:
        if counts2 == [1,1,1,2,2]:
            for i in range(5):
                if h1[i] != h2[i]:
                    return cards.index(h1[i]) > cards.index(h2[i])
        return True

    if counts2 == [1,1,1,2,2]:
        return False
    
    
    for i in range(5):
       if h1[i] != h2[i]:
            return cards.index(h1[i]) > cards.index(h2[i])


listSorted = False
while not listSorted:
    listSorted = True
    for i in range(len(hands)-1):
        if cmp(hands[i], hands[i+1]):
            hands[i], hands[i+1] = hands[i+1], hands[i]
            bids[i], bids[i+1] = bids[i+1], bids[i]
            listSorted = False

out = 0
for i in range(len(hands)):
    out += bids[i] * (i+1)

    print(i+1, hands[i], bids[i])

print(out)
