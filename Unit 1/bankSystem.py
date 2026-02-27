class MarDaGoatBanking:
    def __init__(self, name, password, address, balance):
        self.name = name
        self.password = password
        self.address =address
        self.balance =balance

    def deposit(self, amount):
        self.balance += amount
        print('thanks ' + self.name + ' your new balance is '+ str(self.balance))
    
    def withdrawl(self, amount):
        self.balance -= amount
        print('thanks ' + self.name + ' your new balance is ' +str(self.balance))

    def createAcc(self):
        print('Welcome to MarDaGoatBanking')
        print('Please answer the following questions')
        return

    def closeBankAccount(self, name, password):
        return

    def accessAccount(self,name,password):
        return
acc1= MarDaGoatBanking('jimmy','33223', 'idk lane', 100)
acc2= MarDaGoatBanking('selina','99292','123 ark road', 2000)

#acc1.withdrawl(101)
#acc2.deposit(22)
users=[]

def createAcc():
        print('Welcome to MarDaGoatBanking')
        print('Please answer the following questions')
        name =input('name: ')
        password= input('password: ')
        address= input('Home Adress: ')
        balance = input('how much would you like to put into your account?')
        print('congrats your account has been created')

        acc3 = MarDaGoatBanking(name, password, address, balance)
        users.append(acc3)
        return