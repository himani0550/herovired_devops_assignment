salary=int(input("enter your salary"))
monthly_investment=int(input("enter your monthly wages"))
savings=salary-monthly_investment
EMI=int(input("enter EMI ammount"))
choice=input("enter your choice(monthly/savings/EMI)")
if(choice=='monthly'):
    print(salary-savings)
elif(choice=='savings'):
    print(savings) 
elif(choice=='EMI'):
    print(salary-EMI)  