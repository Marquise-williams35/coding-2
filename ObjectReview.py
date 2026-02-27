'1. A class property is piece of code that stores data from an object'
'2. A class method is code that defines the behavior of an object from a class'


#3:
class student:
  def __init__(self, name, age,teacher,grade):
    self.name = name
    self.age = age
    self.teacher = teacher
    self.grade = grade

Student1 = student('amy', 16,'Mr.mitchel', 'A')
Student2 = student('john', 16,'Ms.Sanchez', 'B')

#4:
class VGC:
    def __init__(self, name, gametype, console, powerlevel):
        self.name = name
        self.Gametype = gametype
        self.console= console
        self.powerlevel= powerlevel