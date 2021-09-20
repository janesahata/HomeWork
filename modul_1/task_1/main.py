value_1 = int(input("enter value1: "))
value_2 = int(input("enter value2: "))
value_3 = int(input("enter value3: "))

operator = input("enter operator ('+' or '*')")
if operator == "+":
  print(value_1 + value_2 + value_3)
elif operator == "*":
  print(value_1 * value_2 * value_3)
else:
  print("bad operator")