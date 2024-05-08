"""
The Open/Closed Principle states that software entities (classes, modules, functions, etc.)
should be open for extension but closed for modification.
This means that you should be able to extend the behavior of a class without modifying
its existing code.
Example: Consider a class representing different shapes with a method to calculate area.
If we need to add a new shape, modifying the existing class violates OCP.
"""

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        # Calculate area of circle
        pass

class Rectangle(Shape):
    def calculate_area(self):
        # Calculate area of rectangle
        pass

"""
To adhere to OCP, we can use inheritance and create a new class for the new shape without modifying
the existing Shape class.
"""

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        # Calculate area of circle
        pass

class Rectangle(Shape):
    def calculate_area(self):
        # Calculate area of rectangle
        pass

class Triangle(Shape):
    def calculate_area(self):
        # Calculate area of triangle
        pass