value_1 = int(input("enter value1: "))
value_2 = int(input("enter value2: "))
operator = input("enter operator ('+' or '-' or '/' or '*'): ")

if operator == "+":
  print(value_1 + value_2)
elif operator == "-":
  print(value_1 - value_2)
elif operator == "*":
  print(value_1 * value_2)
elif operator == "/":
  try:
    print(value_1 / value_2)
  except ZeroDivisionError:
    print("division by zero")
else:
  print("bad operator")
