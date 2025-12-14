from library import Book, User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print(f"dodano książkę: {book}")

    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f"dodano użytkownika: {user}")

    def wyszukaj_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def wyszukaj_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def wypozycz_book(self, user_name, book_title):
        user = self.wyszukaj_user(user_name)
        book = self.wyszukaj_book(book_title)
        if user and book:
            user.wypozycz(book)
        else: print("błąd w wyszukiwaniu")

    def zwroc_book(self, user_name, book_title):
        user = self.wyszukaj_user(user_name)
        book = self.wyszukaj_book(book_title)
        if user and book:
            user.zwroc(book)
        else: print("błąd w wyszukiwaniu")

    def wyswietl_books(self):
        dostepne_books = [book for book in self.books if book.dostepna]
        if not dostepne_books: print("brak")
        else:
            for book in dostepne_books: print(book)

def main():
    lib = Library()

    while True:
        print("1. Dodaj książkę\n2. Dodaj użytkownika\n3. Wypozycz książkę\n4. Zwróć ksiązkę\n5. Wyświetl listę książek\n6. Zakończ")

        wybor = input("wybierz opcję: ")

        if wybor == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok: ")
            lib.add_book(title, author, year)
        elif wybor == "2":
                name = input("Imię: ")
                lib.add_user(name)
        elif wybor == "3":
            user_name = input("Imię użytkownika: ")
            book_title = input("Tytuł książki: ")
            lib.wypozycz_book(user_name, book_title)
        elif wybor == "4":
            user_name = input("Imię użytkownika: ")
            book_title = input("Tytuł książki: ")
            lib.zwroc_book(user_name, book_title)
        elif wybor == "5":
            lib.wyswietl_books()
        elif wybor == "6":
            print("Zamykanie")
            break
        else: print("Niepoprawny wybór")

if __name__ == "__main__":
    main()