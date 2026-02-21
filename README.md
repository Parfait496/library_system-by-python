# library_system-by-python
The system allows books to be added, borrowed, and returned while tracking activity logs and enforcing role-based access control. It is designed to follow Pythonic principles.

# Method Resolution Order(MRO)
Method Resolution Order determines how Python searches for methods in multiple inheritance.

## Scenario

Assume we create a new class called **DigitalBook** that inherits from both **Book** and a hypothetical **Software** class.

class Software:
    def install(self):
        print("Installing software")


class DigitalBook(Book, Software):
    pass

Python calculates MRO using an algorithm called C3 Linearization.

This algorithm ensures:

✔ Child class is checked first
✔ Parent classes are checked left to right
✔ Inheritance order is preserved
✔ No class appears more than once
✔ The order is consistent and predictable

Because DigitalBook inherits like this:
class DigitalBook(Book, Software):
Python searches for methods in this order:
DigitalBook → Book → Software → object

How to View MRO in Python

You can print the MRO using:

print(DigitalBook.__mro__)
output: (DigitalBook, Book, Software, object)

Why MRO Matters

MRO prevents ambiguity in multiple inheritance.
