# Code Nexus
Through the principles of abstract classes, polymorphism, method overriding, and inheritance hierarchies, you will handle different types of data in the same software workflow

## Duck Typing and Polymorphism

In object-oriented programming, polymorphism allows you to treat objects of different types as the same general type. Polymorphism aims to enable code to work with objects of various types through a uniform interface (API), which helps you write more general and reusable code.

You’ll find different forms of polymorphism in object-oriented programming. Duck typing is one of them.

Duck typing enables polymorphism, where you can use objects of different types interchangeably, provided that they implement certain behaviors, also known as their interface. An essential feature of this type of polymorphism is that the objects don’t have to inherit from a common superclass, which makes code less rigid and more adaptable to change.

In Python, duck typing is a pretty popular way to support polymorphism. You just need to decide which methods and attributes a particular class has. Because Python is a dynamically typed language, there are no type-checking restrictions.

## Supporting Duck Typing in Custom Classes
You can support duck typing in your custom classes using two different approaches:

1. Regular methods
For a more elaborate example, say that you want to create classes to read different file formats. You need classes for reading text, CSV, and JSON files.
2. Special methods
Special methods are those whose names start and end with a double underscore. These methods have special meanings to Python. They’re a fundamental part of Python’s object-oriented infrastructure.

Protocols are sets of special methods that support specific features of the language, such as the iterator, context manager, and sequence protocols. Protocols are informal interfaces that are defined in the documentation.

Following established protocols improves your chances of leveraging existing standard-library and third-party code, thanks to duck typing.

To illustrate how you can support duck typing through special methods and protocols, say that you need to write a class that implements a queue data structure. You need your queue to be iterable and support the built-in len() and reversed() functions. It should also support membership tests with the in operator.