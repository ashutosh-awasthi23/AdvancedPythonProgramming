n=int(input("Enter the nth term"))
if n==0 or n==1:
    print(n)
else:
    past=0
    present=1
    i=3
    while i<=n:
        
        future=past+present
        past=present
        present=future
        i=i+1
        
    print(future)