"""
The Facade Design Pattern is a structural design pattern that provides a simplified interface to a complex system of classes, interfaces, or subsystems. It hides the complexity of the system and provides a single interface through which the client can interact with the system.

In Python, the Facade pattern can be implemented using a class that acts as an interface to a set of classes or subsystems. This class provides a unified interface to a larger body of code, simplifying the usage of the system for the client.

Here's a basic outline of how you can implement the Facade Design Pattern in Python:
Identify the Complex Subsystem: Identify a complex system or set of classes/interfaces that need to be simplified for the client.
Create the Facade Class: Define a facade class that provides a unified interface to the complex subsystem. This class delegates the client's requests to the appropriate classes/interfaces within the subsystem.
Define Methods in Facade Class: Define methods in the facade class that represent the high-level operations or functionalities that the client may need.
Use the Facade Pattern: Clients interact with the facade class instead of directly interacting with the subsystem, thus simplifying the usage of the system.

"""

# Complex Subsystem
class Engine:
    def start(self):
        print("Engine started")

class AirConditioner:
    def turn_on(self):
        print("Air conditioner turned on")

class MusicSystem:
    def play_music(self):
        print("Music playing")

# Facade Class
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.air_conditioner = AirConditioner()
        self.music_system = MusicSystem()
    
    def start_car(self):
        print("Car is Starting !!!!")
        self.engine.start()
        self.air_conditioner.turn_on()
        self.music_system.play_music()
        print("Car has Started !!!!")

# Client
car_facade = CarFacade()
car_facade.start_car()
