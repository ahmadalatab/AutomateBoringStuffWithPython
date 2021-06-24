allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
def totalItems(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print("Number of things being brought")
print("Apples - " + str(totalItems(allGuests, 'apples')))
print("Pretzels - " + str(totalItems(allGuests, 'pretzels')))
print("Sandwiches - " + str(totalItems(allGuests, 'ham sandwiches')))
print("Cups - " + str(totalItems(allGuests, 'cups')))
print("Apple Pies - " + str(totalItems(allGuests, 'apple pies')))


