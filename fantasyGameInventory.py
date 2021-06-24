stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def countItems(inventory):
    total = 0
    print("Inventory: ")
    for k, v in inventory.items():
        print(k + " : " + str(v))
        total = total + v

def addToInventory(originallInventory, newInventory):
    for k in newInventory:
        if k in originallInventory:
            originallInventory[k] = originallInventory[k] + 1
        else:
            originallInventory.setdefault(k, originallInventory.get(k, 1))
    countItems(originallInventory)

addToInventory(stuff, dragonLoot)
