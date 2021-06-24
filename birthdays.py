birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print("Enter a name or type quit to exit the program")
    name = input()
    if name == exit:
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
        break
    else:
        print("I do not have the birthday of ", name)
        print("What is their birthday")
        day= input()
        birthdays[name] = day
        print("database updated")
        break
print(birthdays)