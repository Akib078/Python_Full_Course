#multiple Inheritance (Can call multiple classes in a class)

class A:
    def displayA(self):
        print("Its A")

class B:
    def displayB(self):
        print("Its B")

class C(A,B):
    pass

objC = C()

objC.displayA()
objC.displayB()