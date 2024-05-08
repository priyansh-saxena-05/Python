# __init__(self, ...): The constructor method that initializes an object when it is created.

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)  # Output: 10

# __str__(self): The string representation method invoked by the str() function and by printing objects.
# python
# Copy code

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"

obj = MyClass(10)
print(str(obj))  # Output: MyClass instance with value: 10


# __repr__(self): The "official" string representation method invoked by the repr() function and used by the interactive interpreter.
# python
# Copy code

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"MyClass({self.value})"

obj = MyClass(10)
print(repr(obj))  # Output: MyClass(10)


# __eq__(self, other): The equality comparison method invoked by the == operator.
# python
# Copy code


class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1 == obj2)  # Output: False

# __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): Methods for comparison operators <, <=, >, >=, respectively.
# python
# Copy code


class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1 < obj2)   # Output: True
print(obj1 <= obj2)  # Output: True
print(obj1 > obj2)   # Output: False
print(obj1 >= obj2)  # Output: False


# __add__(self, other), __sub__(self, other), __mul__(self, other), __truediv__(self, other): Methods for arithmetic operators +, -, *, /, respectively.
# python
# Copy code

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        return self.value / other.value

obj1 = MyClass(10)
obj2 = MyClass(5)

print(obj1 + obj2)   # Output: 15
print(obj1 - obj2)   # Output: 5
print(obj1 * obj2)   # Output: 50
print(obj1 / obj2)   # Output: 2.0


# __len__(self): Method invoked by the len() function to return the length of an object.
# python
# Copy code

class MyClass:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

obj = MyClass([1, 2, 3, 4, 5])
print(len(obj))  # Output: 5


# __iter__(self), __next__(self): Methods for iteration, used in conjunction with the iter() and next() functions.
# python
# Copy code

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_iter = MyIterator([1, 2, 3, 4, 5])

for item in my_iter:
    print(item)  # Output: 1, 2, 3, 4, 5


# __getitem__(self, key), __setitem__(self, key, value), __delitem__(self, key): Methods for accessing items in objects like dictionaries or lists.
# python
# Copy code


class MyDict:
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

my_dict = MyDict()
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'

print(my_dict['key1'])  # Output: value1

del my_dict['key2']

try:
    print(my_dict['key2'])  # Output: KeyError: 'key2'
except KeyError:
    print("Key does not exist") # Output: None


# __enter__(self), __exit__(self, exc_type, exc_val, exc_tb): Methods used in conjunction with context managers (with statement).
# python
# Copy code
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContextManager() as cm:
    print("Inside the context")