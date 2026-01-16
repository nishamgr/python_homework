# # ---Task 2: A Decorator that Takes an Argument---

# decorator definition
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # calls original func
            result = func(*args, **kwargs) 
            # converts result to the desired type
            return type_of_output(result)
        return wrapper
    return decorator

# decorated funcs
@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

# mainline code
y = return_int()
print(type(y).__name__) # This should print "str"

try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen