#class Person:
#    def pet(self, name, age, color):
#        self.name= name
 #       self.age = age
  #      self.color = color

#p1 = Person('furball', 2 , 'black')

#print(p1.name)
#print(p1.age)
#print(p1.color)

class petCreator:
    def _init_(self, color, age , name, attitude, Type):
        self.color = color
        self.age= age
        self.name= name
        self.attitude = attitude
        self.Type= Type

    def feedPet(self):
        print(self.name + ' is hungry')

    def sleeping(self):
        print(' time for your pet to gts')

    def playtime(self):
        print(' your pet wants to play')

    def bathroom(self):
        print('your pet needs to use the bathroom')

pet_1 = petCreator('white',2,'Kash','calm','Dog')
pet_2 = petCreator('black',6,'phineas','sleepy', 'cat')
pet_3 = petCreator('brown',8,'king','ferocious', 'lion')