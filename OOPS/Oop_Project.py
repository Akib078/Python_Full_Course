'''
Bike Rental System

i. Display available stock
ii. User can rent bike. He will give amount and system will show result (100tk = 1bike)
iii. Exit

'''

class Bike:
    def __init__(self,stock):
        self.stock = stock

    def displayBikes(self):
        print("Total bike = ",self.stock)

    def rentForBike(self,q):
        if q<0:
            print("Enter valid number.")
        elif q>self.stock:
            print("Stock is less than your demand.")
        else:
            self.stock = self.stock - q
            print("Total bill ",q*100,"Taka")
            print("Available stock",self.stock)


while True:
    obj = Bike(100)

    user = int(input('''
                     1. Display available stock
                     2. Rent a bike
                     3. Exit
                     '''))
        
    if user == 1:
            obj.displayBikes()
    elif user == 2:
            n = int(input("Enter quantity : "))
            obj.rentForBike(n)
    else:
         break