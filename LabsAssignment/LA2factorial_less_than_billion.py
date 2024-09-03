def factorialCalculator():
    checker=0
    i=0
    while True:
        fact=1
        if i==0 or i==1 or i==2:
            print(f"factorial of{i} is {i}")
        else:
            j=i
            while j>1:
                fact=fact*j
                j=j-1
            if fact<2000000000:
                print(f"factorial of{i} is {fact}")
            else:
                checker=1
        if checker==1:
            break
        i=i+1
factorialCalculator() 