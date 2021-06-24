pets=["pet1", "pet2", "pet3"]
print("Please enter the pet name ")
petName=input()
if (petName in pets):
    print("Pet already exists")
else:
    pets = pets + [petName]
    print("Added pet")
print("Pet names in the list are: ")
for pet in range(len(pets)):
    print(pets[pet])