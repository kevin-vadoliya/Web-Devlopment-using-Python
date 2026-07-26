# OOP: Inheritance, Polymorphism and Abstract Classes
---

## Objective

Implement and understand **Inheritance, Polymorphism and Abstract
Classes** using Python.

## Theory

### Inheritance

Inheritance allows a child class to acquire the properties and methods
of a parent class.

**Advantages** - Code reusability - Easy maintenance - Better
organization

---

### Polymorphism

Polymorphism means **one interface, many forms**. The same method
behaves differently for different objects.

---

### Abstract Class

An abstract class cannot be instantiated directly. It is created using
Python's `abc` module.

---

## Python Program

``` python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print("Manager Salary = ₹70,000")

class Developer(Employee):
    def salary(self):
        print("Developer Salary = ₹50,000")

class Person:
    def display(self):
        print("Person Details")

class Student(Person):
    def show(self):
        print("Student Information")

print("----- Inheritance -----")
s = Student()
s.display()
s.show()

print("\\n----- Polymorphism -----")
for emp in [Manager(), Developer()]:
    emp.salary()
```

## Output

``` text
----- Inheritance -----
Person Details
Student Information

----- Polymorphism -----
Manager Salary = ₹70,000
Developer Salary = ₹50,000
```

# Explanation

Inheritance

Person is the parent class.
Student inherits the display() method from Person.

Polymorphism

Both Manager and Developer implement the same salary() method.
Different outputs are produced depending on the object.

Abstract Class

Employee is an abstract class.
It contains the abstract method salary().
Manager and Developer must implement the salary() method.

---
