#Rent Calculator in Python
#Inputs from user are: Total Rent, Total food order value,Electricity units,charge per unit
#Output: Total amount you have to pay
rent = int(input("Enter your flat/pg rent in Rupees : "))
food = int(input("Enter total food cost in Rs: "))
electricity_spent = int(input("Enter total electricity used: "))
charge_per_unit = int(input("Enter charge per unit of electricity in your locality: "))
persons = int(input("Enter number of persons living in a flat /pg: "))
total_bill = electricity_spent*charge_per_unit
output = (food + rent+total_bill)//persons
print("Each person will pay rent total as: ",output)
