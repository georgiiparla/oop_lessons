class Library:
    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self, book_name):
        if book_name in self.__books:
            return True
        else:
            return False

    def search_book(self, book_name):
        return self.__check_availability(book_name)

    def return_book(self, book_name):
        self.__books.append(book_name)

    def _checkout_book(self, book_name):
        if book_name in self.__books:
            self.__books.pop(self.__books.index(book_name))
            return True
        else:
            return False


library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
print(library.search_book("Moby-Dick"))
