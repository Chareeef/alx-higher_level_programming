# Python Object-Oriented Programming (OOP) Basics

This project treats key Object-Oriented Programming (OOP) concepts in Python :

## What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that organizes data and behaviors into **objects**. It promotes the idea of modeling real-world entities as objects, making code more modular, reusable, and organized.

## "First-Class Everything"
In Python, everything is an object. This means that functions, classes, and even modules are first-class citizens. They can be assigned to variables, passed as arguments, and returned from functions.

## What is a Class?
A **class** is a blueprint or template for creating objects. It defines attributes (data) and methods (functions) that the objects will have.

## What is an Object and an Instance?
An **object** is an instance of a class. It represents a specific, unique entity that follows the structure defined by its class.

## Class vs. Object (Instance)
- A **class** defines the blueprint.
- An **object** (instance) is a concrete realization of that blueprint.

## What is an Attribute?
An **attribute** is a data field that holds information about an object. Attributes are defined within a class and are accessed using dot notation.

## Public, Protected, and Private Attributes
- **Public Attributes**: Accessible from anywhere.
- **Protected Attributes (Convention)**: Prefixed with a single underscore (_). Limited accessibility.
- **Private Attributes (Convention)**: Prefixed with double underscores (__). Strongest encapsulation, name mangling applied.

## What is `self`?
`self` refers to the current instance of a class. It is used to access instance variables and methods within the class.

## What is a Method?
A **method** is a function defined within a class that can perform actions and interact with object attributes.

## The Special `__init__` Method
`__init__` is a special method, also known as the constructor. It's called when an object is created from a class and initializes its attributes.

## Data Abstraction, Data Encapsulation, and Information Hiding
- **Data Abstraction**: Representing essential features without including the background details.
- **Data Encapsulation**: Bundling data (attributes) and methods (behavior) that operate on the data.
- **Information Hiding**: Restricting access to certain attributes or methods to prevent unintended modification.

## What is a Property?
A **property** is a special attribute accessor method that allows us to get and set values like attributes while controlling access and adding validation.

## Attribute vs. Property in Python
- An **attribute** directly stores data.
- A **property** uses methods to control access and modification.

## Pythonic Way to Write Getters and Setters
Use `@property` decorator for getters and `@<attribute>.setter` for setters to define properties.

## The Special `__str__` and `__repr__` Methods
- `__str__`: Human-readable string representation of an object.
- `__repr__`: Unambiguous string representation used for debugging.

## Difference Between `__str__` and `__repr__`
`__str__` is intended for end-users and `__repr__` is for developers. `__repr__` should ideally create an object identical to the original.

## Class Attribute
A **class attribute** is shared among all instances of a class. It's defined within the class but outside of any methods.

## Object Attribute vs. Class Attribute
- An **object attribute** is specific to an instance.
- A **class attribute** is shared among all instances of the class.

## Class Method
A **class method** is a method that's bound to the class and not the instance.
It is defined using the `@classmethod` decorator.

## Static Method
A **static method** is a method that's defined within a class but doesn't depend on class or instance state.
It is defined using the `@staticmethod` decorator.

## Dynamically Creating Attributes
You can dynamically create new attributes for existing instances of a class by simply assigning values to them.

## Binding Attributes to Objects and Classes
Attributes can be bound to both objects and classes, allowing us to access them using dot notation.

## `__dict__` of a Class and an Instance
`__dict__` is a dictionary that contains all the attributes of a class or an instance, including their names and values.

## How Python Finds Attributes
Python follows a specific order (MRO - Method Resolution Order) to search for attributes in classes and their parent classes.

## Using the `getattr` Function
`getattr(object, attribute_name)` is a built-in function that allows us to dynamically access attributes of an object by name.
