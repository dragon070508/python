print("Welcome to the Simple Calculator!")

print("Enter the first number:")
num1 = float(input())

print("Enter the operation (+, -, *, /):")
operation = input()

print("Enter the second number:")
num2 = float(input())

if operation == "+":
  result = num1 + num2
  print("The result of " + str(num1) + " + " + str(num2) + " is " +
        str(result))
elif operation == "-":
  result = num1 - num2
  print("The result of " + str(num1) + " - " + str(num2) + " is " +
        str(result))
elif operation == "*":
  result = num1 * num2
  print("The result of " + str(num1) + " * " + str(num2) + " is " +
        str(result))
elif operation == "/":
  result = num1 / num2
  print("The result of " + str(num1) + " / " + str(num2) + " is " +
      str(result))