class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.read = False

    def mark_as_read(self):
        self.read = True

    def status(self):
        if self.read:
            print("Read")
        else:
            print("Not read")

def task13():
    book1 = Book("Alchemist", "Paulo Coelho")
    book2 = Book("1984", "George Orwell")
    book3 = Book("Sariq Devona", "O’tkir Hoshimov")
    book4 = Book("Ufq", "Sharof Boshbekov")

    book1.mark_as_read()
    book3.mark_as_read()

    books = [book1, book2, book3, book4]
    for b in books:
        print(f"{b.title}:", end=" ")
        b.status()
