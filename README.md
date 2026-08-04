### **Object-Oriented Programming (OOP) in Python – Short Description**

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into **objects**. An object combines **data (attributes)** and **behavior (methods)**, making programs more modular, reusable, and easier to maintain.

### **Four Main Principles of OOP**

* **Encapsulation** – Bundles data and methods together and restricts direct access to data.
* **Abstraction** – Hides unnecessary implementation details and shows only essential features.
* **Inheritance** – Allows one class to inherit properties and methods from another class.
* **Polymorphism** – Allows the same method or interface to behave differently for different objects.

### **Simple Example**

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

car = Car("Toyota")
car.start()
```

### **Real-World Example**

Think of a **Car**:

* **Attributes:** Brand, Model, Color
* **Methods:** Start, Stop, Accelerate

In OOP, you create a **Car class** and then create multiple **Car objects** (e.g., Toyota, Honda, BMW) from that class.

**Benefits of OOP:**

* ✅ Code reusability
* ✅ Better organization
* ✅ Easier maintenance
* ✅ Improved scalability
* ✅ Real-world modeling
