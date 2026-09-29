class Circle:
    def __init__(self):
        self.radius=int(input("enter radius"))

    def getarea(self):
        print("area",3.14*self.radius**2)
    def getperimeter(self):
        print("perimeter",2*self.radius*3.14)

c=Circle()
c.getarea()
c.getperimeter()

class Account:
    def __init__(self):
        self.accnumber=int(input("enter acc number"))
        self.accname=input("enter acc name")
        self.accbalance=int(input("enter acc balance"))

    def withdraw(self):
        self.withdrawamt=int(input("enter amount to withdraw"))
        self.accbalance=self.accbalance-self.withdrawamt
        print("balance after withdraw:",self.accbalance)
    def deposit(self):
        self.depositamt=int(input("enter amount to deposit"))
        self.accbalance=self.depositamt+self.accbalance
        print("accbalance after deposit",self.accbalance)
    def showbalance(self):
        print("current balance",self.accbalance)
e1=Account()
e1.withdraw()
e1.deposit()
e1.showbalance()