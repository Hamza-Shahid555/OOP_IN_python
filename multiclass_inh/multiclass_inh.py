class A:
    varA= "A class variable"


class B:
    varB= "B class variable"

class C(A,B):
    varC= "C class variable"

c1= C()
print(c1.varA)
print(c1.varB)
print(c1.varC)