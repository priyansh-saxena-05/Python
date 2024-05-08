"""
The Liskov Substitution Principle states that objects of a superclass should be replaceable
with objects of its subclasses without affecting the correctness of the program.
This principle ensures that inheritance is used correctly and subclasses do not violate
the contracts established by their superclasses.
Example: Consider a class representing birds with a fly() method.
If a subclass of Bird, such as Ostrich, cannot fly, it violates LSP.

"""

class Bird:
    def fly(self):
        pass

class Duck(Bird):
    def fly(self):
        # Duck can fly
        pass

class Ostrich(Bird):
    pass  # Ostrich cannot fly

"""
To adhere to LSP, we can refactor the design to avoid introducing subclasses
that violate the behavior defined in the superclass.
"""

class Bird:
    def fly(self):
        pass

class Duck(Bird):
    def fly(self):
        # Duck can fly
        pass

class Ostrich:
    def swim(self):
        # Ostrich swims instead of flying
        pass