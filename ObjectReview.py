'1. A class property is piece of code that stores data from an object'
#A characteristic on a class or object
'2. A class method is code that defines the behavior of an object from a class'
#Methods are functions inside of a class/object

#3:
class Student:
  def __init__(self, name, age,teacher,uniform):
    self.name = name
    self.age = age
    self.teacher = teacher
    self.uniform= uniform
 
  def is_in_uniform(self):
    if self.uniform == False:
      print( self.name + ' has detention')
    else:
       print('This student is ready to start their day')

  def ClassStudy(self):
    print( self.name + ' is studying for ' + self.teacher + "'s class")

student1 = Student('Jimmy',16,'Mr.Johnson',True)
student2 = Student('Nicole',17,'Mrs.Johnson',False)

student1.ClassStudy()
student2.is_in_uniform()


#4:
class VGC:
    def __init__(self, name, gametype, health, powerlevel,ammo):
        self.name = name
        self.Gametype = gametype
        self.health = health
        self.powerlevel = powerlevel
        self.ammo = ammo

    def FireWeapons(self,weapon):
      if self.ammo != 0:
          weapon(self.ammo)
      else:
          print('out of ammo')
    
    def block(self,damage):
       damage = 0
       return damage