# 🎯 OOP: Inheritance, Polymorphism and Abstract Classes

## 📌 Objective

Implement and understand **Inheritance**, **Polymorphism**, and
**Abstract Classes** in Python.

## 🧬 1. Inheritance

> **Definition:** One class acquires the properties and methods of
> another class.

### ✅ Key Points

-   👨‍👩‍👦 Parent Class → Base class
-   👶 Child Class → Derived class
-   ♻️ Code Reusability
-   🛠️ Easy Maintenance

``` python
class Person:
    def display(self):
        print("Person")

class Student(Person):
    pass
```

## 🎭 2. Polymorphism

> Same method, different behavior.

``` python
class Dog:
    def sound(self): print("Bark")

class Cat:
    def sound(self): print("Meow")

for a in [Dog(), Cat()]:
    a.sound()
```

## 🧩 3. Abstract Class

> Cannot be instantiated directly. Created using `abc`.

``` python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
```

## 💻 Complete Program

``` python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self): pass

class Manager(Employee):
    def salary(self): print("Manager Salary = ₹70,000")

class Developer(Employee):
    def salary(self): print("Developer Salary = ₹50,000")

class Person:
    def display(self): print("Person Details")

class Student(Person):
    def show(self): print("Student Information")

s=Student()
s.display()
s.show()

for e in [Manager(), Developer()]:
    e.salary()
```

## ▶️ Output

    Person Details
    Student Information
    Manager Salary = ₹70,000
    Developer Salary = ₹50,000

## 📝 Explanation

-   🧬 **Inheritance:** `Student` inherits `display()` from `Person`.
-   🎭 **Polymorphism:** `salary()` behaves differently for `Manager`
    and `Developer`.
-   🧩 **Abstract Class:** `Employee` defines a common rule using
    `@abstractmethod`.

## ✅ Advantages

-   ♻️ Reusable code
-   📖 Better readability
-   🔧 Easy maintenance
-   📈 Scalable applications

## 🚀 Applications

-   Employee Management
-   Student Management
-   Banking System
-   Hospital System
-   Web Applications

## 🏁 Result

Successfully implemented and understood **Inheritance, Polymorphism, and
Abstract Classes** using Python.
