"""
Problem: Vehicle Inheritance Example
------------------------------------
Demonstrates inheritance in Python:
1. Vehicle is the base class with general functionality.
2. Car and MotorCycle inherit from Vehicle.
3. Each subclass has its own specific attributes and methods.
"""

# Base class
class Vehicle:
    def general_usage(self):
        """
        General usage common to all vehicles
        """
        print("General use: transportation")

# Derived class: Car
class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage(self):
        """
        Specific use case for cars
        """
        print("Specific use: Commute to work, vacation")

# Derived class: MotorCycle
class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a motorcycle")
        self.wheels = 2
        self.has_roof = False
    
    def specific_usage(self):
        """
        Specific use case for motorcycles
        """
        print("Specific use: Racing, road trip solo")

# ------------------ DEMO ------------------
# Instantiate Car
c = Car()
c.general_usage()       # Inherited method
c.specific_usage()      # Car-specific method

# Instantiate MotorCycle
m = MotorCycle()
m.general_usage()       # Inherited method
m.specific_usage()      # Motorcycle-specific method
