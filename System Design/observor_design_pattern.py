"""
The Observer Design Pattern is a behavioral design pattern where an object, known as the subject, maintains a list of its dependents, called observers, and notifies them of any state changes, usually by calling one of their methods. It is often used in situations where changes to one object require changing the state of other objects.

In Python, the Observer Design Pattern can be implemented using classes and their methods. Here's a basic outline of how you can implement the Observer Design Pattern in Python:

Define the Subject Interface: Define an interface (or base class) that specifies the methods for attaching, detaching, and notifying observers.
Implement Concrete Subject: Implement a concrete class that conforms to the subject interface. This class maintains a list of observers and notifies them of any state changes.
Define the Observer Interface: Define an interface (or base class) that specifies the method to be called when the subject notifies observers.
Implement Concrete Observer: Implement concrete classes that conform to the observer interface. These classes define the behavior that should occur when notified by the subject.
Use the Observer Pattern: Create instances of the subject and observers, attach observers to the subject, and notify observers of any state changes.

"""

from abc import ABC, abstractmethod

# Step 1: Define the Subject Interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Step 2: Implement Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

# Step 3: Define the Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Step 4: Implement Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} received update from subject")

# Step 5: Use the Observer Pattern
subject = ConcreteSubject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify()

subject.detach(observer1)

subject.notify()
