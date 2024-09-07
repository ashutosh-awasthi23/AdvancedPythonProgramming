import logging


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' has begun")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' has ended")
        return result
    return wrapper


@log_execution
def logger():
    logging.basicConfig(filename='basicConfig_2024.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')


logger()
