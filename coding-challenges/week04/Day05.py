OOPs stands for Object-oriented programming. OOPs in Pyhton organizes a program around the various objects and well-defined interfaces. 
The OOPs Concepts are abstraction, encapsulation, inheritance, and polymorphism. These concepts aim to implement real-world entities in programs.

Class:
A class is a blueprint that defines the variables and the
methods (Characteristics) common to all objects of a certain kind.
Example: If Car is a class, then Audi A6 is an object of the Car class.
All cars share similar features like 4 wheels, 1 steering wheel,
windows, breaks, etc. Audi A6 (The Car object) has all these
features

The self
1.Class methods must have an extra first parameter in the
method definition. We do not give a value for this parameter when
we call the method, Python provides it
2.If we have a method that takes no arguments, then we still have to
have one argument – the self. See fun() in the above simple example.

The __init__ method
The __init__ method is similar to constructors in
C++ and Java. It is run as soon as an object of a class is
instantiated. The method is useful to do any initialization you want
to do with your object.
