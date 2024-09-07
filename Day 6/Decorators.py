def simple_logger(func):
    def wrapper(*args, **kwargs):

        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result
    return wrapper


@simple_logger
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
