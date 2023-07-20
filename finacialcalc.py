salary=int(input("enter your salary"))
monthly_investment=int(input("enter your monthly wages"))
savings=int(input("enter your monthly wages"))
choice=("enter your choice(monthly/savings):")
if(choice=='monthly'):
    print(salary-savings)

elif(choice=='savings'):
    print(salary-monthly_investment)   