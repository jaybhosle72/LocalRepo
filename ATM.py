class bank():
    def __init__(self,account_id,balance):
        self.account_id=account_id
        self.balance=balance

s=bank(0,0)

    
def entry():
    s.balance=0
    s.account_id=int(input("enter your account no. :"))

def debit():
    amount_debit=int(input("enter amount to debit : "))
    s.balance=s.balance-amount_debit

def credit():
    amount_credit=int(input("enter amount to credit : "))
    s.balance=amount_credit+s.balance
    
def display():
    print("account no = ",s.account_id)
    print("balance number : ",s.balance)

def exit():
    print("exiting")
    

while True:
    print("1.for entry\n2.for credit ammount\n3.for debit ammount\n4.for show balance\n5. for exit")
    choice=int(input("enter your choice : "))

    if choice==1:
        entry()
    elif choice==2:
        credit()
    elif choice==3:
        debit()
    elif choice==4:
        display()
    elif choice==5:
        exit()
        break
    else:
        print("invalide input")