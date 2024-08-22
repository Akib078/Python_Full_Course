#Encapsulation : Making something private or not giving full access.
    #An object variables should not always be directly accessible.
    #The methods can ensure the correct values are set. If an incorrect value is set, the method can return an error

class Student:
    __name = "Akib"        #__ is used to make variable or function private

    def __init__(self): 
        print(self.__name)         #Constructor is used to call private variables and functions
        self.__displayInfo()

    def __displayInfo(self):
        print("Welcome")

obj = Student()


