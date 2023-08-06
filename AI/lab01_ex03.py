# Exercise: Dictionaries
# Use 'dir' and 'help' to learn about the function
# you can call on dictionaries and implement it
d = {'key1': 'value1', 'key2': 'value2'}
print("-" * 40)
print(dir(d))
help(d.clear)
print("-" * 40)

# ============================================
# (ii)Write a Python script to concatenate
# following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = dic1 | dic2 | dic3
print(new_dic)
