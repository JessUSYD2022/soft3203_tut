class Book:
    """
    Represents a book with a title, author, and price.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        price (float): The price of the book; must be a non-negative number.
    """

    def __init__(self, title: str, author: str, price: float) -> None:
        """
        Initialises a new book instance with the given title, author, and price.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book; must be a non-negative number.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        """Returns a string representation of the book."""
        return f'{self.title} by {self.author} for ${self.price}'

    def __repr__(self) -> str:
        """Returns a string that could be used to recreate the book object."""
        return f"Book('{self.title}','{self.author}','{self.price}')"

    def apply_discount(self, percentage: int) -> None:
        """
        Applies a given percentage discount to the book's price.

        Parameters:
            percentage (int): The discount percentage to apply.
        """
        discount = percentage / 100
        self.price *= discount


class BookshopInventory:
    """
    Manages a collection of books as an inventory for a bookshop.

    Attributes:
        inventory (list[Book]): A list that stores instances of `Book`.
    """

    def __init__(self) -> None:
        """Initialises a new bookshop inventory with an empty list of books."""
        self.inventory = []

    def add_book(self, book: Book) -> None:
        """
        Adds a `Book` instance to the inventory.

        Parameters:
            book (Book): The book to add to the inventory.

        Raises:
            Exception: If the book title already exists in the inventory.
        """

        for existing_book in self.inventory:
            if existing_book.title == book.title:
                raise Exception(f"{book.title} already exists in the inventory.")
        self.inventory.append(book)

    def remove_book(self, index: int) -> None:
        """
        Removes the book at the specified index from the inventory.

        Parameters:
            index (int): The index of the book to remove.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index >= len(self.inventory) or index < 0:
            raise IndexError("The index is out of bounds.")
        else:
            del self.inventory[index]

    def apply_bulk_discount(self, percentage: int) -> None:
        """
        Applies a given percentage discount to all books in the inventory.

        Parameters:
            percentage (int): The discount percentage to apply.
        """
        for book in self.inventory:
            book.apply_discount(percentage)

    def __len__(self) -> int:
        """Returns the total number of books in the inventory."""
        return len(self.inventory)

    def __getitem__(self, index: int) -> Book:
        """
        Allows retrieval of a book at a specific index.

        Parameters:
            index (int): The index of the book to retrieve.

        Returns:
            Book: The book at the specified index.
        """
        return self.inventory[index]

    def searchBookBytitle(self,title:str):
        bookList = []
        for book in self.inventory:
            if book.title == title:
                bookList.append(book)

        return bookList

    def searchBookByauthor(self,author:str):
        bookList = []
        for book in self.inventory:
            if book.author == author:
                bookList.append(book)

        return bookList


    def sort_by_title(self,ascending=False):
        self.inventory.sort(key=lambda book: book.title, reverse=not ascending)

    def sort_by_price(self, descending=False):
        self.inventory.sort(key=lambda book: book.price, reverse=descending)

    def run_cli(self):
        inventory = BookshopInventory()
        while True:
            print("\nAvailable commands: add, discount, search, sort, exit")
            command = input("Enter command: ").strip().lower()
            if command == "add":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                price = float(input("Enter book price: "))
                inventory.add_book(Book(title, author, price))
                print("Book added.")
            elif command == "discount":
                percentage = int(input("Enter discount percentage: "))
                inventory.apply_bulk_discount(percentage)
                print("Discount applied.")
            elif command == "search":
                criterion = input("Search by (title/author): ").strip().lower()
                query = input("Enter search query: ")
                if criterion == "title":
                    results = inventory.searchBookBytitle(query)
                elif criterion == "author":
                    results = inventory.searchBookByauthor(query)
                else:
                    print("Invalid search criterion.")
                    continue
                print("Search results:")
                for book in results:
                    print(book)
            elif command == "sort":
                criterion = input("Sort by (title/price): ").strip().lower()
                order = input("Order (asc/desc): ").strip().lower()
                descending = order == "desc"
                if criterion == "title":
                    inventory.sort_by_title(descending)
                elif criterion == "price":
                    inventory.sort_by_price(descending)
                else:
                    print("Invalid sort criterion.")
                    continue
                print("Inventory sorted.")
            elif command == "exit":
                print("Thank You!!")
                break
            else:
                print("Invalid command.")


book = Book(title="A", author="A", price=1)
C = Book(title="A", author="A", price=1)
inventory = BookshopInventory()
## B.add_book(C) correctly raise Exception: A already exists in the inventory
print(book)
len(inventory)
print(f"{book}")
len(inventory)
#print(inventory[0])
book.apply_discount(10); print(book)
inventory.add_book(book); print(inventory)
for book in inventory: print(book)
print("The price of the book is: {:.2f}".format(book.price))
inventory.sort_by_title(); print(inventory)
inventory.run_cli()
