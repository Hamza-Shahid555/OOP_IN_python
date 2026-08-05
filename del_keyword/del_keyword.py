class Student:
    def __init__(slef, name):
        self.name=name

s1=Student("Alice")
print(s1.name)

del s1.name
print(s1.name)  # This will raise an AttributeError since the name attribute has been deleted