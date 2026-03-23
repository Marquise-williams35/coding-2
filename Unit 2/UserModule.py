class Car:
    def __init__(self, model, year, MPH, color):
        self.model = model
        self.year= year
        self.MPH = MPH
        self.color = color
    def carModel(self):
        print(self.model + ' is the model of the car')

    def MakeYear(self):
        print(str(self.year) + ' is the year the car was made')
    
    def Speed(self):
        print('this car can go ' + str(self.MPH) + ' in 8 seconds')

    def CarColor(self):
        print('The color of the '+ self.model + ' is ' + self.color)

Vehicle1 = Car('Sports car', 2026, 0-60, 'Blue')
vehicle2=  Car('Suv',2018, 0 -40, 'black')
Vehicle1.MakeYear()
vehicle2.Speed()
