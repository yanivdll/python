def addToInventory(inventory, addedItem):
    #loop through dragonLoot
    #for every item, add to the inventory
    #addition to inventory should be done so if it exist already, do a +1
    #if not - add with value of 1 (setdefault?)

    for i in addedItem:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
    return inventory

def displayInventory(inventory):

    totalItems = 0

    for k, v in inventory.items():
        print('Key: ' + k + '. Value: ' + str(v))
        totalItems += v

    print('Total numner of items: ' + str(totalItems))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
