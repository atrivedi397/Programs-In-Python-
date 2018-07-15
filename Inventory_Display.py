def display_inventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print(f'\nTotal number of items : {total_items}')


def dragon_loot(inventory, added_items):
    for k in added_items:
        if k not in inventory.keys():
            inventory.setdefault(k, 0)

        else:
            inventory[k] = inventory[k]+1

    return inventory


D = {'rope': 1,
     'torch': 6,
     'gold coin': 42,
     'dagger': 1,
     'arrow': 12}

display_inventory(D)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
D = dragon_loot(D, dragonLoot)
display_inventory(D)
