hrs = float(input("Enter Hours:"))
h = float(hrs)
rate = float(input("enter rate"))
over40 = hrs % 40
hoursOver40 = 0
payOver40 = 0
if over40 > 0:
    hoursOver40 = over40
    payOver40 = float(hoursOver40) * (rate * 1.5)
    print("pay over 40", payOver40)
    
total = ((hrs - over40) * rate) + (payOver40)
print(total)

