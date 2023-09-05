# Python Objects, References, Mutability, and Immutability

## Introduction

Welcome to the README for our *python-everything_is_object* project! In this document, we'll provide a concise overview of essential concepts related to Python objects, references, mutability, and immutability. Understanding these concepts is fundamental to becoming proficient Python programmers.

## Python Objects

- **Objects:** In Python, everything is an object. Objects can be values, data structures, or instances of classes.

- **References:** Variables in Python are references to objects. They point to the memory location where the object is stored.

## Mutability and Immutability

### Mutable Objects

- **Mutable Objects:** Mutable objects can be modified after creation.

- **Examples:** Lists, dictionaries, and sets are mutable. We can add, remove, or change elements in them.

- **Modification:** Changes to mutable objects are reflected in the same object, as we modify them in place.

### Immutable Objects

- **Immutable Objects:** Immutable objects cannot be modified after creation.

- **Examples:** Integers, floats, strings, and tuples are immutable. Any operation that appears to modify them actually creates a new object with the updated value.

## Identifying Mutability

- To check if an object is mutable or immutable, we can attempt to modify it and see if the original object changes or if a new object is created.

## References and Aliasing

- Aliasing occurs when two or more variables reference the same object in memory.

- We can use the `is` keyword to check if two variables are aliases for the same object.

## Passing Variables to Functions

- Python uses a "pass-by-object-reference" mechanism when passing variables to functions.

- Mutable objects can be modified inside functions, and changes are reflected outside the function.

- Immutable objects cannot be modified inside functions; changes result in new objects.

## Conclusion

This project provides an overview of critical concepts related to Python objects, references, mutability, and immutability. Understanding these concepts is essential for writing efficient and reliable Python code. We can explore these concepts through practical examples to solidify our knowledge and become proficient Python programmers.

Happy coding!
