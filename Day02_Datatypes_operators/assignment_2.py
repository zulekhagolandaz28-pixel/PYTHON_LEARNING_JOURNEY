#Q2 Take input in Celsius and convert it into Fahrenheit and Kelvin.
celsius=float(input("Enter temperature in Celsius: "))
fahrenheit=(celsius*9/5)+32
kelvin=celsius+273.15
print("Temperature in Fahrenheit is: ", fahrenheit)
print("Temperature in Kelvin is: ", kelvin)

#Q2 Write a program that takes total bill amount and number of friends as input. Calculate how much each friend has to pay. Also print data type of each variables used.
total_bill=float(input("Enter total bill amount: "))
num_friends=int(input("Enter number of friends: "))
amount_per_friend=total_bill/num_friends
print("Each friend has to pay: ", amount_per_friend)
print("Data type of total_bill: ", type(total_bill))
print("Data type of num_friends: ", type(num_friends))
print("Data type of amount_per_friend: ", type(amount_per_friend))