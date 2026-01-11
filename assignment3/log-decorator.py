import logging

# ---Task 1: Writing and Testing a Decorator---

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# define decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # call the original function
        result = func(*args, **kwargs)

        # parameters for logging
        function_name = func.__name__
        positional_parameters = list(args) if args else "none"
        keyword_parameters = dict(kwargs) if kwargs else "none"

        # log message
        log_message = (
            f"function: {function_name}\n"
            f"positional parameters: {positional_parameters}\n"
            f"keyword parameters: {keyword_parameters}\n"
            f"return: {result}\n"
        )

        logger.log(logging.INFO, log_message)

        return result
    return wrapper

# func defined and decorated
@logger_decorator
def greetings():
    print("Hello, World!")

@logger_decorator
def var(*args):
    return True

@logger_decorator
def another_func(**kwargs):
    return logger_decorator

# calling the func
greetings()
var(1, 2, 3)
another_func(a=10, b=15)


# ---Task 2: A Decorator that Takes an Argument---
