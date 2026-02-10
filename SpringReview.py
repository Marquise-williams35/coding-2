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
DiscountPriceChecker()
    