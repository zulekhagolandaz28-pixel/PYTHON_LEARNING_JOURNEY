print("Day 2 - Data type and Operators")

#Q1 Create variables containing a string, an integer, a float, a boolean
name="Zulekha"
age=20
height=165.5
is_student=True
print("name:",type(name))
print("age:",type(age))
print("height:",type(height))
print("is student:",type(is_student))

#Q2 Create two numbers and calculate: addition subtraction multiplication division  modulus
num1 = 20
num2 = 6
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

#Q3 Create two numbers and use comparison operators to check: which number is greater, which is smaller, whether they are equal, whether they are different
num1 = 20
num2 = 10
print("Is num1 greater than num2?", num1 > num2)
print("Is num1 smaller than num2?", num1 < num2)
print("Are the numbers equal?", num1 == num2)
print("Are the numbers different?", num1 != num2)

#Q4 Create variables representing something like: age has_id. Use and, or, and not to create a few logical expressions.
age = 20
has_id = True
print("Age is 18 or above and has ID:", age >= 18 and has_id)
print("Age is below 18 or has ID:", age < 18 or has_id)
print("Does not have ID:", not has_id)

#Q5 Create variables for: product price, quantity, amount paid. Calculate the total bill and remaining amount.
#Then use comparison operators to check whether the amount paid is enough to cover the bill.
product_price = 50
quantity = 3
amount_paid = 200
total_bill = product_price * quantity
remaining_amount = amount_paid - total_bill
print("Total bill:", total_bill)
print("Remaining amount:", remaining_amount)
print("Amount paid is enough:", amount_paid >= total_bill)