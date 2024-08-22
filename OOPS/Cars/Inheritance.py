class car():
    def __init__(self,modelName,releaseDate,price):
        self.modelName = modelName
        self.releaseDate = releaseDate
        self.price = price

class SuperCar(car):
    def __init__(self, modelName, releaseDate, price):
        super().__init__(modelName, releaseDate, price)

toyota = SuperCar("Axio",2009,1200000)

print(toyota.price)