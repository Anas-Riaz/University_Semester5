# (Write a list comprehension which, from a list, generates
# a lowercased version of each string that has length
# greater than five.

my_list = ["Hello", "world", "One piece", "Laugh Tale"]
lower_case = [s.lower() for s in my_list if len(s) > 5]
print(lower_case)

# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Tea pink']
new_list = [value for index, value in enumerate(sample_List) if index not in [0, 4, 5]]
print(new_list)
