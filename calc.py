#Program maeks a simple calculator

#This function adds two numbers
def add(x,y):
    return x + y

#This function subtracts two numbers
def subtract(x,y):
    return x - y

#This function multiples two numbers
def multiply(x,y):
    return x * y

#This function dividess two numbers
def divide(x,y):
    return x / y

num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))

print("Sum:",add(num1,num2))
print("Difference:",subtract(num1,num2))
print("Product:",multiply(num1,num2))
print("Quotient:",divide(num1,num2))