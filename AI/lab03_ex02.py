# I. You have collected information about cities in your province.
# You decide to store each city’s name, population, and mayor in a file.
# Write a python program to accept the data for a number of cities from the keyboard
# and store the data in a file in the order in which they’re entered.

with open("cities.txt", "w") as file:
    while True:
        city_name = input("Enter city name (leave blank to exit): ")
        if not city_name:
            break
        city_population = input("Enter city population: ")
        city_mayor = input("Enter city mayor: ")
        file.write(f"{city_name},{city_population},{city_mayor}\n")

# Write a python program to create a data file student.txt and append the message
# “Now we are AI students”s
with open("student.txt", "a") as file:
    file.write("Now we are AI students")