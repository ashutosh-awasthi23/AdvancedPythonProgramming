li = [ "Fizz" if x % 3 == 0 and x % 5 != 0
        else "Buzz" if x % 5 == 0 and x % 3 != 0
        else "FizzBuzz" if x % 3 == 0 and x % 5 == 0
        else x
        for x in range(1, 21) ]

print(li)
