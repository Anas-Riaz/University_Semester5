# (ii)Write a Python program to count the number of strings
# where the string length is 2 or more and the
# first and last character are same from a given list of strings.
sample_List = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in sample_List:
    if item[0] == item[-1]:
        count += 1
print("Result : {}".format(count))