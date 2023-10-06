# Decorator to print function names
def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Applying the decorator to functions
@print_function_name
def function1():
    print("Inside function1")

@print_function_name
def function2():
    print("Inside function2")

# Calling the decorated functions
function1()
function2()
