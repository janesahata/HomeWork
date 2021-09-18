value_1 = int (input("value: "))
value_2 = int (input("value: "))
operator = input("operator (+\-\/\*): ")
if operator == "+":
    if value_1 and value_2:
        print(int(value_1) + int(value_2))
    else:
        print('bad')
elif operator == "-":
    if value_1 and value_2:
        print(int(value_1) - int(value_2))
    else:
        print('bad')
if operator == "*":
    if value_1 and value_2:
        print(int(value_1) * int(value_2))
    else:
        print('bad')
if operator == "/":
    if value_1 and value_2:
        print(int(value_1) / int(value_2))
    else:
        print('bad')