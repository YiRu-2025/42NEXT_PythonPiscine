# Object-Oriented Garden Systems
Create tools to manage community gardens efficiently through data-driven approaches.

Skills: Python Fundamentals, data management system
Target:
- Understanding how Python programs are structured and executed
- Organizing data using an object-oriented approach
- Creating reusable code components
- Building systems that can adapt and extend
- Protecting data integrity in collaborative environments
- Designing scalable software architectures

This project focuses on Python programming concepts, starting from basic program structure and progressing to Object-Oriented Programming. Each exercise introduces new features while building a cohesive garden management system. Later exercises will reuse concepts from earlier ones.
The exercises order is as below:
1. planting your first seed
2. garden data organizer
3. plant growth simulator
4. plant factory
5. garden security system
6. specialized plant types
7. garden analytics

# Concept of Python Fundamentals
## Class and Object
1. What is a Class in Python?

A class is a blueprint or template used to create objects.

Think of a class as a design for something, and objects as the actual things created from that design.

Class = Car Design Drawing
Object = An actual car built from that design

The class defines:

What data an object has (attributes)
What actions an object can do (methods)

2. What Does a Class Contain?

A class typically contains:

Attributes (variables/data)
Methods (functions)
Constructor (__init__)
Class variables (shared by all objects)

Q: The difference and use of instance attribute and class variable.

instance attribute belongs to each object individually, used when values differ per object.

class variables are shared by all objects, used when values should be shared.

e.g. for students at a school, they have their own student id (instance attribute), but study at the same school (class variable)

3. what are the characteristics of a Class?
The four classic characteristics of OOP are:
- Encapsulation: Bundle data and method together.
- Inheritance: A child class can reuse code from a parent class.

```c
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
```
Dog class automatically gets `eats()`

- Polymorphism: same method name. different behavior
In different classes, can define the same method name, still act with different behavior.
Method overriding.

- Abstraction: Hide unnecessary details and expose only important features.

4. difference between Python and C++ for Class
C++ has access control in Class:
- public : accessible everywhere
- protected : accessible inside the class and derived classes
- private : accessible only inside the class
