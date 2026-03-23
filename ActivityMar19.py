# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 

#The difference between a python class and a object is that a class defines what the code can do and a object is an example of that class

# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.

# An object property is a variable that goes with a object and a object method is a function that goes along with an object


# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 

class Student:
    def __init__(self,name,age,classes,GPA,grade):
        self.name=name
        self.age=age
        self.classes=classes
        self.GPA=GPA
        self.grade=grade

    def GPA_Checker(self):
        if self.GPA >= 3.7:
            print('Thats incredible')
        elif self.GPA >= 3.4:
            print('Thats great')
        elif self.GPA >= 2.0:
            print('ehh its ok')
        else:
            print('could definatly be better')

    Student1 = Student('jenny',17, 'environmental science', 3.7, 'sophmore')
    print(student1.GPA_Checker)