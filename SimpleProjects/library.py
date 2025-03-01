class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    
    def addBooks(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books.The books are")
        for books in self.books:
            print(books)

l1=Library()
l1.addBooks("harry")
l1.addBooks("kanana")
l1.showInfo()
