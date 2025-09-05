kwh = int(input("Enter the KW Hours used: "))
rate1=0.07633 #dollars
rate2=0.09259 #dollars
if kwh <=1000:
    amount = kwh * rate1
else:
    amount = (1000 * rate1) + ((kwh-1000)*rate2)

print("amount owed is $", amount)