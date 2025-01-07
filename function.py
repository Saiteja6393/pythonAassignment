# Specifications
# Receive the following arguments from the user:
# Kilometers to drive
# Liters-per-kilometer usage of the car
# Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console
 
# 2.  While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. 
# If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.
 
# for both the assignment you have to create functions
 


def trip_cost(km,lit_per_km,fuel_price):
    total=km*lit_per_km*fuel_price
    return total
km=int(input("enter kms to drive:"))
lit_per_km=float(input("enter liters per kilometer:"))
fuel_price=float(input("enter fuel price per litre:"))
print(trip_cost(km,lit_per_km,fuel_price))


def total_expences(qty,price_per_item):
    if qty>=10:
        #10% discount applied if qty is more than 10
        total=(qty*price_per_item-(qty*price_per_item*0.1))
        return total
    else:
        return qty*price_per_item
qty=int(input("enter the quantity:"))
price_per_item=int(input("enter the price per qyantity:"))
print(total_expences(qty,price_per_item))

