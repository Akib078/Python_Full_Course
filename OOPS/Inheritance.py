#Single Inheritance (One class gets access of one another class)

class A():
    def displayA(self):
     print("Display A")

class B(A):
    def displayB(self):
        print("Display B")

obj1 = B()

obj1.displayA()
obj1.displayB()

#Multi level Inheritance (One class to another to another class)

class C(B):
   def displayC(self):
      print("Display C")

obj2 = C()

obj2.displayA()
obj2.displayB()

