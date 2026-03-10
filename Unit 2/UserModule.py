class Car:
    def __init__(self, model, year, MPH):
        self.model = model
        self.year= year
        self.MPH = MPH

    def carModel(self):
        print(self.model + ' is the model of the car')

    def MakeYear(self):
        print(self.year + int('is the year the car was made'))


Vehicle1 = Car('sports car', 2026, 0-60)

Vehicle1.MakeYear()
