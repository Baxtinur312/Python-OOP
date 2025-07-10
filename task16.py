class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print("O‘qilgan")
        else:
            print("O‘qilmagan")

def task16():
    b1 = Book("Alchemist", "Paulo Coelho")
    b2 = Book("1984", "George Orwell")
    b3 = Book("Sariq Devona", "O’tkir Hoshimov")
    b4 = Book("Ufq", "Sharof Boshbekov")
    b5 = Book("Shum bola", "G'afur G'ulom")

    b1.mark_as_read()
    b3.mark_as_read()

    books = [b1, b2, b3, b4, b5]
    print("Barcha kitoblarning holati:")
    for b in books:
        print(f"{b.title}:", end=" ")
        b.status()

    print("\nO‘qilgan kitoblar:")
    for b in books:
        if b.is_read:
            print(b.title)