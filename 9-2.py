f = open("9.txt").readlines()

ans = 0
for line in f:
    seqends = []
    seq = [int(i) for i in line.split(" ")]
    while set(seq[i+1]-seq[i] for i in range(len(seq)-1)) != set([0]):
        seqends.append(seq[-1])
        seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    
    seq = seq + [seq[0]]


    for i in range(len(seqends)):
        oldseq = seq[:]
        seq = [seqends[-i-1]]
        for i in range(len(oldseq)):
            seq = [seq[0]-oldseq[-1-i]] + seq
    ans += (seq[0])

    
print(ans)
