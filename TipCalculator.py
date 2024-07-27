print("---Welcome to the Tip Calculator---")
total_bill=float(input("What was the Total Bill? $"))
tip=float(input("How much Tip would you like to give? 10%, 12%, 15%? %"))
people=int(input("How many people to split the bill? "))
pay= ((total_bill * tip // 100)+(total_bill) )//people
print("Each person should pay: $", int(pay))