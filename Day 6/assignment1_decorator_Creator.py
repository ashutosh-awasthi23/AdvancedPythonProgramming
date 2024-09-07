def simpledecorator(func):
    def wrapper(*args,**kwargs):
        print(f"The name of the function is {func.__name__}")
        result=func(*args,**kwargs)
        print(f"The name of the function is {func.__name__}")
        return result
    return wrapper
@simpledecorator
def greet(name):
    print(f"Hello, I'm {name}")

name="Ashutosh Awasthi"
greet(name)