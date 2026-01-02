from codecs import raw_unicode_escape_decode
from pprint import pprint

raw_books = [
    {
        "title": "  the hobbit ",
        "author": "tolkien",
        "genre": "Fantasy",
        "price": "10.99",
    },
    {"title": "1984", "author": "Orwell", "genre": "Dystopian", "price": 8.50},
    {
        "title": "Brave New World",
        "author": "Huxley",
        "genre": "dystopian",
        "price": "9.25",
    },
    {"title": "The Catcher in the Rye", "author": "Salinger", "price": "7.99"},
    {
        "title": "Fahrenheit 451",
        "author": "Bradbury",
        "genre": "Dystopian",
        "price": 6.75,
    },
    {
        "title": "The Fellowship of the Ring",
        "author": "Tolkien",
        "genre": "Fantasy",
        "price": "12.50",
    },
]


# Define Class
class Books:
    def __init__(self, title, author, genre, price):
        self.title = str(title).strip().title()
        self.author = str(author).strip().title()
        self.genre = str(genre).strip().title() if genre is not None else "Other"
        self.price = float(price)


class Library:
    def __init__(self, raw_books):
        # Convert dictionary to book objects
        self.books = []
        for book in raw_books:
            genre = book.get("genre", "Other")
            # Call Books class
            book = Books(
                title=book.get("title", ""),
                author=book.get("author", ""),
                genre=genre,
                price=book.get("price", 0.0),
            )


def average_price(self):
    total = 0
    for book in raw_books:
        total += book["price"]
    avg = total / len(raw_books)
    print(f"Average price: ${avg}")


def min_price(self):
    minimum = min(book["price"] for book in raw_books)
    print(f"Minimum price: ${minimum}")


def max_price(self):
    maximum = max(book["price"] for book in raw_books)
    print(f"Maximum price: ${maximum}")


def group_by_genre(self):
    groups = {}

    for book in raw_books:
        if "genre" not in book:
            book["genre"] = "Other"
        else:
            genre = book["genre"]

            if genre not in groups:
                groups[genre] = []
            groups[genre].append(book)
    return groups


def summary_by_genre(self):
    groups = self.group_by_genre

    for genre, books in groups.items():
        count = len(books)
        avg = sum(b["price"] for b in books) / count
        print(f"{genre} - Count: {count}, Avg Price: ${avg}")
