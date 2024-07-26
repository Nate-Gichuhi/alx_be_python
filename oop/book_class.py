class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return  "{self.title} by {self.athor},published in {self.year}"
    
    def __repr__(self):
        return Book(self.title, self.author, self.year)
    
    def __del__(self):
        self.close(Book(title=self.title, author=self.author, year=self.year))

