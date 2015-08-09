playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):

    totalItems = 0

    for k, v in inventory.items():
        print('Key: ' + k + '. Value: ' + str(v))
        totalItems += v

    print('Total numner of items: ' + str(totalItems))
        
    
    return True



displayInventory(playerInventory)
    
