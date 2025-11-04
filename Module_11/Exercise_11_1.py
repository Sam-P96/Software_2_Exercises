# Publication
# Book or Magazine(name, author, page count, chief editor)
# print info for both

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_c, c_editor):
        super().__init__(name)
        self.author = author
        self.page = page_c
        self.c_editor = c_editor
        self.type = "Book"

    def print_information(self):
        print(f"""Name : {self.name}
Author: {self.author}
Page Count: {self.page}
Chief Editor: {self.c_editor}
Type: {self.type}
""")

class Magazine(Publication):
    def __init__(self, name, author, page_c, c_editor):
        super().__init__(name)
        self.author = author
        self.page = page_c
        self.c_editor = c_editor
        self.type = "Magazine"

    def print_information(self):
        print(f"""Name : {self.name}
Author: {self.author}
Page Count: {self.page}
Chief Editor: {self.c_editor}
Type: {self.type}
""")

dd = Book("Donald Duck", "Aki Hyyppä", 31, "Samnap Peo")
c6 = Magazine("Compartment No. 6", "Rosa Likson", "Suspicious Editor", 192)

dd.print_information()
c6.print_information()