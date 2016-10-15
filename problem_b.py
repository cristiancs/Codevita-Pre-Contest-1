def new_final_capital(nMonths, rate, monthlyInv, currentCap = 0):
    if (nMonths == 0):
        return currentCap
    currentCap = new_final_capital(nMonths-1, rate, monthlyInv,
                                   monthlyInv + currentCap + ((currentCap+monthlyInv) * (rate/(100*12))))
    return round(currentCap)
try:
    monthly_deposit = round(float(input()), 11)
except:
    print("Invalid Input")
    exit()
if monthly_deposit <= 0:
    print("Invalid Input")
    exit()
try:
    rate = round(float(input()), 11)
except:
    print("Invalid Input")
    exit()
if rate < 0:
    print("Invalid Input")
    exit()
try:
    months = int(input())
except:
    print("Invalid Input")
    exit()
print("Final_Amount "+str(new_final_capital(months, rate, monthly_deposit)))