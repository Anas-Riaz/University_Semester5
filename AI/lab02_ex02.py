time_taken = int(input("Enter time (like how many hours) : "))

if 2 <= time_taken < 3:
    print("Worker is highly efficient")
elif 3 <= time_taken < 4:
    print("Worker needs to improve speed")
elif 4 <= time_taken < 5:
    print("Worker needs training to improve speed")
else:
    print("Worker should leave the company")
