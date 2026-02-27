def DiscountPriceChecker():
    itemPrice= int(input('please enter item price '))
    if itemPrice >= 50 and itemPrice <= 75:
        discount = .15
        sum = itemPrice * discount
        total = itemPrice - sum
        print('this is ypur final sum ' + str(total))
    elif itemPrice >= 75:
        discount = .25
        sum = itemPrice * discount
        total = itemPrice - sum
        print('this is your final sum ' + str(total))
    else:
        print('sorry, you do not get a discount.')
#DiscountPriceChecker()

def jobFair(gpa,age):
    if gpa >= 90 and age >= 17:
        print('You qualify for the job fair')
    else:
        print('sorry you dont qualify for the job fair')
#jobFair(90,2)
  myGrades = [76, 87, 79, 84, 100, 81, 99, 72, 100, 98, 91]
def GPA():
    for grade in myGrades:
        if grade < 85:
            myGrades.remove(grade)
        print(myGrades)
GPA()