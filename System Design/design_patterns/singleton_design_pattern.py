"""
The Singleton Design Pattern ensures that a class has only one instance and provides a global point of access to that instance. It is often used when exactly one object is needed to coordinate actions across the system, such as configuration objects or logging systems.

In Python, the Singleton pattern can be implemented using a class with a private constructor and a class method that returns the instance of the class. Here's a basic outline of how you can implement the Singleton Design Pattern in Python:
Create the Singleton Class: Define a class with a private constructor and a class variable to hold the instance of the class.
Define a Class Method: Define a class method that returns the instance of the class. This method checks if an instance of the class already exists. If it does, it returns the existing instance; otherwise, it creates a new instance and returns it.
"""

class Singleton:
    _instance = None
    
    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Singleton instance already exists. Use getInstance() method to get the instance.")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Example usage:
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(singleton1 is singleton2)  # Output: True
