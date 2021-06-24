catNames=[]
while True:
    print("Enter the name of the " + str(len(catNames) + 1) + " cat or type exit to quit the program.")
    catName=input()
    if catName == "exit":
        break
    else:
        catNames = catNames + [catName]
        print("Successfully added " + catName + " to the list")
    print("Current cats are :")
    for cat in catNames:
        print(cat)
