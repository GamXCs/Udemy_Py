from operator import inv
from pprint import pp, pprint

# Dictionary to simulate an inventory
inventory = {
    "apple": {"quantity": 5, "price": 0.75},
    "orange": {"quantity": 7, "price": 0.25},
    "pear": {"quantity": 8, "price": 0.45},
    "plum": {"quantity": 3, "price": 1.75},
    "grapefruit": {"quantity": 1, "price": 0.55},
}


# function to add item
def add_item(item, quantity, price):
    inventory.setdefault(item, {"quantity": 0, "price": price})
    inventory[item]["quantity"] += quantity


# function to remove item
def remove_item(item, quantity):
    # Check if item exists
    if item not in inventory:
        print(f"{item} is not in inventory.\n")
        return
    current = inventory[item]["quantity"]

    if quantity > current:
        inventory[item]["quantity"] = 0
    else:
        inventory[item]["quantity"] -= quantity


# def remove_item(item):
#     return


# function to compute total inventory value
# function to update quantity


# Test add_item function
# add_item("apricot", 2, 1.33)
# add_item("apple", 2, 0.75)
# pprint(inventory)

remove_item("apple", 3)  # normal case
remove_item("apple", 50)  # should stop at 0
remove_item("marker", 2)  # missing item case (message)
pprint(inventory)
