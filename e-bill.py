print("""This is a simple python program to calculate your monthly electricity bill in sri lanka.
P.S It calculates your bill for 30 days
Tarrif:Domestic""")

#cost of when cosumption is below 60kWh

c1=8.00
c2=10.00 
fc1=120.00 #fixed cost of electricity 1-30kWh
fc2=240.00 #fixed cost of electricity when 31-60kWh

#cost when consumption is above 60kWh

c3=16.00 #0-60kWh (old price 7.85)
c4=16.00 #61-90kWh(old price 10.00)
fc3=360.00 #fixed cost of electricity when counsumption is 61-90kWh(old)
c5=50.00#91-180kWh (old price 27.75)
fc4=960.00 #fixed cost of electricity when consumption is 91-180kWh
c6=75.00
fc5=1500.00 #fixed cost of electricity when consumption is above 180kWh

units=int(input("Enter the number of units: "))
days=int(input("Enter the number of days: "))
cost=0
tcost=0

if(units<=60):
    if(units<=30):
        cost=(units*c1)
        print(int(units), "x", c1, "=", units*c1)
        tcost=(cost+fc1)
    elif(units>30):
        cost=(30*c1)+((units-30)*c2)
        print("30 x ", c1, "=", (30*c1))
        print(int(units-30), "x", c1, "=", (units-30)*c2)
        tcost=cost+fc2


elif(units>60):
    if(units<=60):
        cost=(units*c2)
        print(int(units), "x", c4, "=", units*c4)
        tcost=(cost+0)
    elif(units in range(61,90)):
        cost=(60*c3)+((units-60)*c4)
        print("60 x ", c3, "=", (60*c3))
        print(int(units-60), "x", c4, "=", (units-90)*c4)
        tcost=cost+fc3
    elif(units in range(91,180)):
        cost=(60*c3)+(30*c4)+((units-90)*c5)
        print("60 x ", c3, "=", (60*c3))
        print("30 x ", c4, "=", (30*c4))
        print(int(units-90), "x", c5, "=", (units-90)*c5)
        tcost=cost+fc4
    elif(units>180):
        cost=(60*c3)+(30*c4)+(90*c5)+((units-180)*c6)
        print("60 x ", c3, "=", (60*c3))
        print("30 x ", c4, "=", (30*c4))
        print("90 x ", c5, "=", (90*c5))
        print(int(units-180), "x", c6, "=", (units-180)*c6)
        tcost=cost+fc5

print("The usage cost is : Rs. ", cost)        
print("The total cost is : Rs. ", tcost)