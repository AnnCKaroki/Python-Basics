# The basic unit of code is objects

# Classes are blueprints that defines the attributes and methods that an object will possess

# example:

class Dog:
    def __init__(self, name): #constructor
        self.name = name

    def bark(self): #method
        print("Woof!")

dog1 = Dog("Snow") #an object
print(dog1.name)
dog1.bark()

# Inheritance is when a class inherits attributes and methods from another class. The child class takes both the parents sttributes and its own then we call the parent's class constructor so that the child can now inherit/possess the attributes of the parent.
# A constructor initializes the attributes
# Class variables are shared by all objects and are defined in the class itself outside any methods
# To do that we use a special constructor(super.__init__(here we list the parent attributes) )
# Afterwards the child attributes are defined well.
# Example:

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def describe(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def describe(self):
        return f"A {self.make} {self.model} with {self.num_doors} doors."

class Bicycle(Vehicle):
    def __init__(self, make, model, type):
        super().__init__(make, model)
        self.type = type
    def describe(self):
        return f"A {self.make} {self.model} ({self.type} bicycle)."


# Polymorphism: Many forms, same interaction; objects respond differently to the same message based on their type.

# Abstraction: Showing 'what' an object does, while hiding 'how' it does it.

# Encapsulation is about creating self-contained, robust objects where the internal workings are managed securely and interactions are controlled through a clear, public interface.
