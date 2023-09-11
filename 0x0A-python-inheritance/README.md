# Python Inheritance and Related Concepts

In Python, inheritance is a fundamental concept of Object-Oriented Programming (OOP). It allows us to create new classes (subclasses) that inherit attributes and methods from existing classes (superclasses or base classes). This promotes code reusability, organization, and the creation of class hierarchies. Let's explore some key concepts:

## Superclass, Base Class, and Parent Class

- **Superclass, Base Class, or Parent Class**: These terms refer to the class from which other classes inherit properties and behaviors.

## Subclass

- **Subclass**: A subclass is a class that inherits attributes and methods from a superclass. It can also add new attributes or methods and override inherited ones.

## Listing Attributes and Methods

- To list all attributes and methods of a class or instance, we can use the `dir()` function.

## Adding New Attributes

- An instance in Python can have new attributes added at any time by assigning values to them.

## Inheriting from a Class

- To inherit from a class, we use the following syntax:
  ```python
  class ChildClass(ParentClass):
      # ChildClass's attributes and methods
  ```

## Multiple Inheritance

- We can define a class with multiple base classes by separating them with commas in the class definition.

## Default Inheritance from `object`

- Every class in Python inherits from the `object` class by default. Even if not explicitly mentioned, this inheritance is implicit.

## Method and Attribute Overriding

- To override a method or attribute inherited from the base class, we define a method or attribute with the same name in the subclass.

## Purpose of Inheritance

- The purpose of inheritance is to promote code reusability, create a hierarchy of classes, and organize code efficiently.

## Built-in Functions

- `isinstance()`: Used for type checking an object's class or classes.
- `issubclass()`: Checks if a class is a subclass of another class.
- `type()`: Returns the type of an object (used for basic type checking).
- `super()`: Invokes methods from the parent class in the context of the subclass.
