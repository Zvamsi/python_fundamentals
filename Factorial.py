num=int(input("Enter a number"))

while num>0:
    digit=num%10
    start=1
    while start <= digit:
        print(start)
        no=1
        fact=1
        while start > 0:
            fact*=start
            print("hello")
            start-=1
        print(fact)
        start+=1
    num=num//10