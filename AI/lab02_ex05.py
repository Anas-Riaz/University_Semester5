print("printing 1-100")
for i in range(101):
    print(i, end='\t')
# ----------------------------------------------
print()
print("tables from 1-10")
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end='\t')
    print()
# ----------------------------------------------
print()
print("Reverse order from 10-1")
for i in range(10, 0, -1):
    print(i, end='\t')
# ---------------------------------------------
print()
print("Even numbers from 1-10")
for i in range(2, 11, 2):
    print(i, end='\t')
# ---------------------------------------------
print()
total = 0
for i in range(100, 201):
    total += i
print("total = {}".format(total))
