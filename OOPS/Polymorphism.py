#Polymorphism means same function name (but different signatures) being uses for different types.

'''
# Overloading : (Means same function but acting differently according to different parameters given)

class Area:
    def calculate(self,x=None,y=None):
        
        if x!= None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1 = Area()
obj1.calculate()
obj1.calculate(2)
obj1.calculate(2,3)

'''


#Overriding : (Means when a class is inheritated then with same functions then child function will be overriden with parent's function)

class parent:
    def display(self):
        print("im from parent")

class child(parent):
    def display(self):
        # super().display()   #super() is used to call parent function to overcome overriding
        print("im from child")

obj = child()
obj1 = parent()
obj1.display()