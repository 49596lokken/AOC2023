f = open("9.txt").readlines()


ans = 0
for line in f:
    seqstarts = []
    seq = [int(i) for i in line.split(" ")]
    while set(seq[i+1]-seq[i] for i in range(len(seq)-1)) != set([0]):
        seqstarts.append(seq[0])
        seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    
    seq = seq + [seq[0]]

    for i in range(len(seqstarts)):
        oldseq = seq[:]
        seq = [seqstarts[-i-1]]
        for i in range(len(oldseq)):
            seq.append(oldseq[i] + seq[-1])
    ans += (seq[-1])

    
print(ans)
