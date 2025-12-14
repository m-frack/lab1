class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.dostepna = True

    def __str__(self):
        return self.title

class User:
    def __init__(self, name):
        self.name = name
        self.wypozyczone = []

    def __str__(self):
        return self.name

    def wypozycz(self, book):
        if book.dostepna:
            book.dostepna = False
            self.wypozyczone.append(book)
            print(f"wypożyczono {book.title}")
        else: print(f"{book.title} nie jest dostępna")

    def zwroc(self, book):
        if book in self.wypozyczone:
            book.dostepna = True
            self.wypozyczone.remove(book)
            print(f"oddano {book.title}")
        else: print(f"ten użytkownik nie wypożyczał {book.title}")