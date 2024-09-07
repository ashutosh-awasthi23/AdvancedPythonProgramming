import logging

def logging_decorator(log_level):
    logging.basicConfig(filename="app.log", filemode='w', level=log_level, format='%(asctime)s-%(levelname)s-%(message)s')
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(f"starting function {func.__name__}")
            try:
                result = func(*args, **kwargs)
            except Exception:
                print('function is not working')
            logging.info(f"finishing function {func.__name__}")
            return
        return wrapper
    return decorator




@logging_decorator('INFO')
def logggg():
    logging.debug("dkfjasgkuaetrdfh")
    return logging.info('inside of the logggg funtion')




logggg()