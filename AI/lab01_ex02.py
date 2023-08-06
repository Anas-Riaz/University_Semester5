# Try out some string functions listed in dir
s = 'No where to run'
print("s.capitalize() : ",s.capitalize())
print("s.count('n')", s.count('n'))
print("s.find('e')", s.find('e'))
print("s.upper()", s.upper())
print("s.split()", s.split())
print("s.replace('t', 'j')", s.replace('to', 'from'))


print("-"*40)

# Write a Python program to convert temperatures
# to and from celsius,


def Fahrenheit(temp):
    f = (temp * 9/5) + 32
    print("Temperature in Fahrenheit is : {}".format(f))


def Celsius(temp):
    c = (temp-32) * 5/9
    print("Temperature in Celsius is : {}".format(c))


temp = float(input("Enter temp : "))
choice = input("Enter temperature degree (press c or f) : ")
if choice == 'c'.casefold():
    Fahrenheit(temp)
elif choice == 'f'.casefold():
    Celsius(temp)

