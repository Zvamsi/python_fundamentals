n=1
for i in range(1,4):
    for j in range(1,4):
        for k in range(n+1,1000):
            n=k
            count=0
            for l in range(1,k+1):
                if k%i==0:
                    count+=1
            if count==2:
                print(k,end='')
                break
    print()