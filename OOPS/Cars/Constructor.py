class car():
    def __init__(self,modelName,releaseData,price):
        self.modelName = modelName
        self.releaseData = releaseData
        self.price = price

honda = car("city",2005,800000)
toyota = car("axio",2009,1200000)

print(honda.__dict__) #prints whole data as dictionary
print(toyota.__dict__)

toyota.color = "black" #add new element in the class
print(toyota.__dict__)
        