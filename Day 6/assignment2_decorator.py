# Calculate execution time
import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        x = time.time()
        result = func(*args, **kwargs)
        y = time.time()
        print(f"Duration of function '{func.__name__}': {y - x} seconds'")
        return result

    return wrapper


def log_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"Starting function '{func.__name__}'..")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' function ended.")
        return result

    return wrapper


@log_execution_time
@log_func_name
def greet(name):
    time.sleep(2)
    print(f"Hello, {name}")


greet("Alice")






