class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self): 
        return f"Title:{self.title}"

    def __str__(self):
        return f"Author:{self.author}" 
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(self, title, author)
        self.file_size = file_size

class PrintBook(Book):
      def __init__(self, title, author, page_count):
           super().__init__(self, title, author)
           self.page_count = page_count
          
class Library:
    books = [
        Book,
        Ebook,
        PrintBook
    ]
    def add_book(self, books):
         self.books.append(books)

    def list_books(self):
        print(Book(self.title, self.author))
        print(Ebook(self.title, self.author, self.file_size))
        print(PrintBook(self.title, self.author, self.page_count))


