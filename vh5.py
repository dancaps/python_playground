d = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'flask', 'water', 'water']

def displayInventory(inventory):
    item_total = 0
    print('Inventory:')
    for v in inventory:
        print(str(inventory.get(v)) + ' ' + v)
        item_total += inventory.get(v)
    print('The total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

displayInventory(addToInventory(d, dragonLoot))