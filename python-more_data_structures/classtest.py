#!/usr/bin/python3
class Car:

    #class attribute
    brand = "Toyota"

    def __init__(self,name,transmission,model,distance,fuel):
        self.name = name
        self.transmission = transmission
        self.model = model
        self.distance = distance
        self.fuel = fuel

    def mileage(self):
            consumption = self.distance / self.fuel
            print(f"{float(consumption)} kilometres per litre is the consumption of a {self.name}.")

corolla = Car("Corolla", "Manual", "2018", 180, 20)
lc200 = Car("LC200", "Manual", "2018", 180, 40)
camry = Car("Camry", "Automatic", "2019", 200, 20)
corolla.mileage()
lc200.mileage()
camry.mileage()

