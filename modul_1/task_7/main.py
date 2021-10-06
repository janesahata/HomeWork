
def find_equal(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                c.append(i)
                print(c)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

print(find_equal(a, b))

