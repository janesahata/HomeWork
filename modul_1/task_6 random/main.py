import random

for _ in range(10):
    r_i = random.randint(1, 10)
    if r_i % 2 == 0:
        print("Parne ", r_i)
    else:
        print("Ne Parne ", r_i)
