try:
  value_1 = float(input("monthly salary UAH: "))
  value_2 = float(input("monthly loan payment UAH: "))
  value_3 = float(input("utility bills UAH: "))
  print(value_1-value_2-value_3)
except Exception:
  print("bad number")
