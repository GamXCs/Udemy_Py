book_inventory = {
    "1984": {"quantity": 12, "price": 9.99},
    "Brave New World": {"quantity": 5, "price": 12.50},
    "Dune": {"quantity": 3, "price": 15.00},
    "Foundation": {"quantity": 0, "price": 8.75},
    "The Hobbit": {"quantity": 20, "price": 7.50},
}

""" Create 4 functions to do the following:
    1. add a book
    2. remove a book
    3. get book quantity
    4. total value of books
    Bonus: low stock of books that returns/prints
    books where the quantity is less than the threshold (parameter)
    Bonus: most valuable book (largest quantity * price
    """


def add_book(book, quantity, price):
    book_inventory.setdefault(book, {"quantity": 0, "price": price})
    book_inventory[book]["quantity"] += quantity


def remove_book(book, quantity):
    if book not in book_inventory:
        print(f"{book} is not currently in inventory.")
        return

    current_inv = book_inventory[book]["quantity"]

    if quantity > current_inv:
        book_inventory[book]["quantity"] = 0
    else:
        book_inventory[book]["quantity"] -= quantity


def set_book_quantity(book, quantity):
    if book not in book_inventory:
        print(f"{book} is not currently in inventory.")
        return

    if quantity < 0:
        quantity = 0

    book_inventory[book]["quantity"] = quantity


def total_book_value():
    total = 0
    for book, data in book_inventory.items():
        quantity = data["quantity"]
        price = data["price"]
        total += quantity * price
    return total
