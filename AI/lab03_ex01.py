import datetime

# Python program to integers_square and cube every number in a given list of integers using Lambda.

numbers = [x for x in range(10)]
integers_square = [(lambda a: a ** 2)(x) for x in numbers]
integers_cube = [(lambda a: a ** 3)(x) for x in numbers]
print("ex01 (i)")
print("numbers", numbers)
print("numbers", integers_square)
print("numbers", integers_cube)
print("-" * 40)


# Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda string, char : True if string[0] == char else False
print("ex01 (ii)")
print(starts_with("banana", 'b'))
print("-" * 40)


# Python program to extract year, month, date and time using Lambda.

now = datetime.datetime.now()
get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day
get_time = lambda x: x.time()
print("ex01 (iii)")
print("Year:", get_year(now))
print("Month:", get_month(now))
print("Day:", get_day(now))
print("Time:", get_time(now))
