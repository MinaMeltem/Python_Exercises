#SIMPLE RESTAURANT BILL CALCULATOR

# Asking user to enter the price
meal = float(input("Enter the price: "))

#Adding tax and tip, and calculate the total
tax = meal * 0.18
tip = meal * 0.20
total = meal + tax + tip

#Displaying the total amount
print ( "Your total is : "+ str(total))