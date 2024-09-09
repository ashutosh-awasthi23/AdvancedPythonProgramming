import time
import logging

def decorator2(func):
    logging.basicConfig(
        filename="decoratorExam.log",
        level="DEBUG",
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    def wrapper(*args,**kwargs):
        x=time.time()
        func(*args,**kwargs)
        y=time.time()
        logging.debug(f"The execution time of the function is {y-x} seconds")
    return wrapper

def decorator1(func):
    logging.basicConfig(
        filename="decoratorExam.log",
        level="DEBUG",
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    def wrapper(*args,**kwargs):
        logging.debug(f"The name of the function is {func.__name__}")
        func(*args,**kwargs)
    return  wrapper


@decorator2
@decorator1
def mainfunction():
    time.sleep(3)
    print("Hello Friends")
mainfunction()