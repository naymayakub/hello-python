    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        self.balance=0
        self.deposits=[]
        self.withdraw=[]
        self.loan=0
   
    def deposit(self,amount):
        now=datetime.now()

        object={"time":now,"amount":amount}

        self.balance=self.balance+amount
        self.deposits.append(object)
        print ("Dear {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_no,self.balance))

    def withdraw_cash(self,amount):
        now=datetime.now()
        object={"time":now,"amount":amount}

        if amount<self.balance:
            self.balance=self.balance-amount
            print ("Dear {}, you have withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_no,self.balance))
            self.withdraw.append(object)
        else:
            print('dear customer you do not have sufficient balance.your current balance is {},thank you'.format(amount))


    def check_bal(self):
        self.balance=self.balance
        print ("Dear {}, you have a balance of Ksh{}.Thank you for using Mpesa".format(self.name,self.balance))
            
    def my_deposits(self):
        for deposit in self.deposits:
            time=deposit["time"].strftime("%A,%B,%d,%Y")
            amount=deposit["amount"]
            print("{}-{}".format(time,amount))

    def my_withdawals(self):
        for withdraw_cash in self.withdraw:
            time=withdraw_cash["time"].strftime("%A,%B,%d,%Y")
            amount=withdraw_cash["amount"]
            print("{}-{}".format(time,amount))

    def get_loan(self,loan):
        self.loan=loan
        if self.deposits.append(amount)>5:
            print("Dear customer you are now able to apply for a loan")
        elif self.loan>0:
            print("Dear customer to get another loan,you need to pay the existing loan first.Thank you")   

        else:
            print("Dear customer you are unable to get a loan")     

    
        
    
        
                        
