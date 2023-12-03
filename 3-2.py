f = open("3.txt").read().splitlines()



symbols = []

tot  = 0
for i, line in enumerate(f):
    for j, sym in enumerate(line):
        if sym == "*":
            #We have a symbol
            numNumbers = 0
            gearRatio = 1
            for k in range(-1, 2):
                a = 0
                for l in range(-1,2):
                    if a != 0:
                        a -=1 
                        continue
                    if 0 <= i+k and i+k < len(f) and l+j >= 0 and l+j < len(f[i]):
                        if f[i+k][j+l].isnumeric():
                            num = f[i+k][j+l]
                            m = 1
                            while j+l-m >= 0 and f[i+k][j+l-m].isnumeric():
                                num = f[i+k][j+l-m] + num
                                m += 1
                            
                            m = 1
                            while j+l+ m < len(f[i]) and f[i+k][j+l+m].isnumeric():
                                num += f[i+k][j+l+m]
                                m+=1
                            a = m-1
                            gearRatio *= int(num)
                            numNumbers += 1
            if numNumbers == 2:
                tot += gearRatio



    

print(tot)



