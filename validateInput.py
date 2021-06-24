while True:
    print("Enter your age: ")
    age=input()
    if age.isdecimal():
        break
    else:
        print("Please enter a number for your age.")

while True:
    print('Select a password. (Letters and numbers only) ')
    password=input()
    if password.isalnum():
        break;
    else:
        print("Your password should only contain letters and numbers")