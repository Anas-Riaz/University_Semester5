i = 0
while i <= 100:
    print(i)
    i += 1
print("-"*80)
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
print("-"*80)
i = 10
while i >= 1:
    print(i)
    i -= 1
print("-"*80)
i = 0
while i <= 10:
    print(i)
    i += 2
print("-"*80)
i = 100
total = 0
while i <= 200:
    total += i
    i += 1
print(total)
