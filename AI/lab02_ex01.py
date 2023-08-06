# --------------------------------------
length = int(input("Enter length : "))
height = int(input("Enter height : "))
width = int(input("Enter width : "))

volume = length * width * height
print(volume)

if 1 <= volume <= 10:
    print("Extra small")
elif 11 <= volume <= 25:
    print("Small")
elif 26 <= volume <= 75:
    print("Medium")
elif 76 <= volume <= 100:
    print("Large")
elif 101 <= volume <= 250:
    print("Extra large")
elif volume >= 251:
    print("Extra-Extra Large")
