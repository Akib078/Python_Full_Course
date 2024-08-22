#Parent Class

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)


#Child class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        