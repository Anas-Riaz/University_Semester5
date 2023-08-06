known_password = 'ABC$123'
username = input('Enter your username: ')
password = input('Enter your password: ')

if password.casefold() == known_password.casefold():
    print('Welcome!')
else:
    print("I don't know you.")
