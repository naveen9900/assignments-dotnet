def createWallet(balance,name):
    balanceDeposit=0
    balanceSpend=0
    amt=int(input("Enter Amount: "))
    
    def deposit(amt):        
        nonlocal balance
        nonlocal balanceDeposit
        balanceDeposit=balance+amt
        print
       
    deposit(amt)
    
    def spend(amt):
        nonlocal balance
        nonlocal balanceSpend
        if(balance>amt):
            balanceSpend=balance-amt
        else:
            print("Invalid Sufficient")
            
    spend(amt)
    li=[balanceDeposit,balanceSpend]
    li2=[deposit(200),spend(300)]
    return li
    
listb=createWallet(1000,"Aatisha")
print(listb) 