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