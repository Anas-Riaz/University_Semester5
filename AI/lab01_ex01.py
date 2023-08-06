# Exercise python input /output Basic operations
# #Write a Python program to swap 4 variables values
# (input four values).
def swap(a, b, c, d):
    a, b, c, d = d, c, b, a
    print("a = {}, b = {}, c ={}, d = {}".format(a, b, c, d))


def get_value():
    for index in range(4):
        data = int(input("Enter value : "))
        list_of_data.append(data)


list_of_data = []
get_value()
a, b, c, d = list_of_data
swap(a, b, c, d)
