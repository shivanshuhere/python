# Python OOPs Notes (Detailed)

## 1. Overview

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects". It allows structuring programs in a way that bundles data and behavior together.

### Key Concepts:

-   **Class**: Blueprint for creating objects.
-   **Object**: Instance of a class.
-   **Encapsulation**: Hiding internal state and requiring all interaction to be performed through an object's methods.
-   **Inheritance**: Mechanism to define a new class based on an existing class.
-   **Polymorphism**: Ability to use different classes interchangeably through a common interface.
-   **Abstraction**: Hiding complex implementation details and showing only essential features.

## Why OOP?

-   Helps in organizing large codebases
-   Encourages code reuse through inheritance
-   Enhances readability and maintainability
-   Mimics real-world entities

## 2. `self` Variable

`self` represents the instance of the class. It's used to access attributes and methods of the class.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
```

-   `self` is not a keyword, just a naming convention.
-   Must be the first parameter in instance methods.

## 3. Constructor

The `__init__` method is a special method called automatically when an object is created. It is used for initializing object attributes.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## 4. Types of Variables

-   **Instance Variable**: Belongs to the object.
-   **Class Variable**: Shared among all objects.

```python
    class Student:
        school = "ABC School"  # class variable, we can access these variables using obj and name of the class

        def __init__(self, name):
            self.name = name  # instance variable

    obj = Student()
    obj.name # accessing instance var
    Student.school # accessing class var
```

## 5. Namespaces

Namespace is a container for names (variables/functions).

### Types:

-   **Built-in Namespace**: Python built-in names like `len()`, `id()`.
-   **Global Namespace**: Names defined at the module level.
-   **Enclosing Namespace**: Names in nested functions.
-   **Local Namespace**: Names defined inside a function.

```python
global_var = 10

def func():
    local_var = 5
```

## 6. Classes and Objects

-   **Class**: Template for creating objects.
-   **Object**: Real-world entity based on the class.

```python
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
```

## 7. Inheritance

Allows a class to inherit properties and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```

## 8. Types of Methods

-   **Instance Methods**: Access instance variables.
-   **Class Methods**: Access class variables.
-   **Static Methods**: General utility methods without accessing class or instance variables.

## 9. Instance Methods

Used to access/modify object state. They use `self`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
```

## 10. Static Methods

Defined using `@staticmethod`. Doesn’t access class or instance data.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

## 11. Class Methods

Defined using `@classmethod`. Uses `cls` instead of `self`.

```python
class School:
    school_name = "ABC"

    @classmethod
    def get_school_name(cls):
        return cls.school_name
```

## 12. Accessing Attributes

We use dot (`.`) operator to access object attributes.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("Toyota")
print(c.brand)
```

Bonus `super()` method

```python
super().method_name()
```

## 13. Built-in Class Attributes

-   `__dict__`: Dictionary of class namespace.
-   `__doc__`: Class documentation string.
-   `__name__`: Class name.
-   `__module__`: Module name.
-   `__bases__`: Base classes.

```python
print(Car.__dict__)
```

## 14. Destroying Objects

`__del__` method is called when object is deleted or destroyed.

```python
class Test:
    def __del__(self):
        print("Object destroyed")

t = Test()
del t
```

## 15. Abstract Classes and Interfaces

Used to define a blueprint for other classes. Implemented using `abc` module.

-   Cannot be instantiated directly.
-   Used to ensure derived classes implement required methods.

## 16. Abstract Methods and Class

-   **Abstract Method**: Defined in abstract class, must be implemented in child class.
-   **Abstract Class**: Cannot be instantiated.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
```

## 17. Interface in Python

Python doesn’t have built-in interfaces like Java, but we use abstract classes to create interface-like behavior.

```python
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass
```

## 18. Abstract Classes and Interfaces

Both help in designing better structured and reusable code.

-   Abstract classes can have some implementation.
-   Interfaces (using abstract classes) force derived classes to implement methods.

```python
class Document(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class PDF(Document):
    def read(self):
        print("Reading PDF")

    def write(self):
        print("Writing PDF")
```

---

## Tips

### Key Syntax :

-   `def` to define functions
-   `class` to define classes
-   `@staticmethod`, `@classmethod` for method types

### Practice :

-   Create a class for `BankAccount` with deposit, withdraw, and balance methods.
-   Create a class `Animal` and derive `Dog` and `Cat` classes from it.

### Built-in Functions:

-   `type()`, `isinstance()`, `dir()`, `help()`
