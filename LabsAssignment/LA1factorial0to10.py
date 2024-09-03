def factorialCalculator():
    i=0
    while i<=10:
        fact=1
        if i==0 or i==1 or i==2:
            print(f"factorial of{i} is {i}")
        else:
            j=i
            while j>1:
                fact=fact*j
                j=j-1
            print(f"factorial of{i} is {fact}")
        i=i+1
        

factorialCalculator() 