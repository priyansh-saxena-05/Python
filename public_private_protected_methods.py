class Car:
    def __init__(self, make, model, year):
        self.make = make  # Public attribute
        self.model = model  # Public attribute
        self._engine_started = False  # Protected attribute
        self.__vin_number = "123ABC"  # Private attribute

    # Public method
    def start_car(self):
        if not self._engine_started:
            self._engine_started = True
            print(f"The {self.make} {self.model} is now started.")
            self.__check_vin()  # Call private method within the class
        else:
            print(f"The {self.make} {self.model} is already started.")

    # Protected method
    def _stop_car(self):
        if self._engine_started:
            self._engine_started = False
            print(f"The {self.make} {self.model} is now stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

    # Private method
    def __check_vin(self):
        print(f"Checking VIN number: {self.__vin_number}")

# Usage of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Public method can be accessed and used freely
my_car.start_car()  # The Toyota Camry is now started.

# Protected method can be accessed but is generally intended for internal use
my_car._stop_car()  # The Toyota Camry is now stopped.

# Private method cannot be accessed directly from outside the class
# my_car.__check_vin()  # This will raise an AttributeError

# But it can be accessed using name mangling (not recommended)
my_car._Car__check_vin()  # Checking VIN number: 123ABC
