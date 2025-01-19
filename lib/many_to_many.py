# Book class  
class Book:  
    all_books = []  # Class variable to keep track of all book instances  

    def __init__(self, title):  
        self.title = title  
        self._contracts = []  # Instance variable to keep track of contracts for this book  
        Book.all_books.append(self)  

    def contracts(self):  
        """Return a list of contracts related to this book."""  
        return self._contracts  

    def authors(self):  
        """Return a list of authors related to this book via contracts."""  
        return [contract.author for contract in self._contracts]  

# Author class  
class Author:  
    def __init__(self, name):  
        self.name = name  
        self._contracts = []  # Private list to store contracts  
        self._books = []      # Private list to store books  

    def add_contract(self, contract):  
        self._contracts.append(contract)  
        self._books.append(contract.book)  # Automatically associate book when contract is signed  

    def contracts(self):  
        """Return all contracts associated with the author."""  
        return self._contracts  

    def books(self):  
        """Return a list of books associated with this author, derived from contracts."""  
        return self._books  

    def sign_contract(self, book, date, royalties):  
        """Create a contract for this author and the specified book."""  
        contract = Contract(self, book, date, royalties)  
        self.add_contract(contract)  # Automatically track this contract  
        return contract  

    def total_royalties(self):  
        """Calculate total royalties from contracts."""  
        return sum(contract.royalties for contract in self._contracts)

# Contract class  
class Contract:  
    all_contracts = []  # Class variable to keep track of all contract instances  

    def __init__(self, author, book, date, royalties):  
        if not isinstance(author, Author) or not isinstance(book, Book):  
            raise Exception("Invalid Author or Book instances.")  
        if not isinstance(date, str):  
            raise Exception("Date must be a string.")  
        if not isinstance(royalties, int) or royalties < 0:  
            raise Exception("Royalties must be a non-negative integer.")  

        self.author = author  
        self.book = book  
        self.date = date  
        self.royalties = royalties  
        Contract.all_contracts.append(self)  # Keep track of all contracts  

        # Ensure the contract is added to both Author and Book  
        author._contracts.append(self)  
        book._contracts.append(self)  

    @classmethod  
    def contracts_by_date(cls, date):  
        """Return all contracts that have the same date as the date passed into the method."""  
        return [contract for contract in cls.all_contracts if contract.date == date]