# class bank ,3 method (accnt creation(name,acc number,minimum balance),
# amound widrow(amound,print balance),
# deposit(amound,print total balance))

class Bank:
    Bank_name="SBI"
    def account_creation(self,name,acc_number):
        self.name=name
        self.acc=acc_number
        self.min=5000
        self.balance=self.min
    def deposit(self,amound):
        self.amnd=amound
        self.balance+=self.amnd
        print("your account",Bank.Bank_name," has credited",self.amnd)
        print("total balance",self.balance)

    def widrow(self,amound1):
       self.amnt1=amound1
       if (self.amnt1>self.balance):
           print("insuffient balance")
       else:
           self.balance -= self.amnt1
           print("your account",Bank.Bank_name," has debited",self.amnt1)
           print("total balance", self.balance)

ob=Bank()
ob.account_creation("vinay",121212)
ob.deposit(10000)
ob.widtrow(5000)