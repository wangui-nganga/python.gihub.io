# parent class
class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title

    def display_info (self):
        return f"The Title {self.title} ,Author {self.author}"

    # child class/derived class
    # super ni inheritance

class LibraryBook(Book):
    def __init__(self,author,title,copies_available):
        super().__init__(author,title)
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed.Copies left {self.copies_available}"
        else:
            return f"No of copies unavailable {self.title}"
    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. copies left: {self.copies_available}"
    # usage example


book1 = LibraryBook("Adrian","Inheritance",20)
book2 = LibraryBook("Monalisa","Here Again",5)


print(book1.display_info())
print(book1.borrow_book())
print(book1.return_book())

print(book2.display_info())
print(book2.borrow_book())
print(book2.return_book())





