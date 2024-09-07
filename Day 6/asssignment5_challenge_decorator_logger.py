import logging


def log_to_file(log_level=logging.INFO):
    logging.basicConfig(
        filename="challenge.log",
        level=log_level,
        format='%(asctime)s-%(levelname)s-%(message)s'
    )

    def decorator(func):
        if log_level == logging.ERROR:
            logging.error("This is an error msg")

        else:
            logging.debug('This is a debug message')
            logging.info('This is an info message')
            logging.warning('This is a warning message')

        def wrapper(*args, **kwargs):
            print(f"Starting{func.__name__}")
            result = func(*args, **kwargs)
            print(f"Finished{func.__name__}.")
            return result

        return wrapper

    return decorator


@log_to_file(log_level=logging.ERROR)
def logger():
    pass


logger()
