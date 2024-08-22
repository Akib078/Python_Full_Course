class Student:
    def __init__(self):
        self.__name = ""

    def getName(self):          #Getter
        return self.__name
    
    def setName(self,n):        #Setter
        self.__name = n

obj = Student()
obj.setName(input("Enter name : "))
A = obj.getName()
print(A)