class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_book_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}"
    
    def get_age(self, current_year):
        return current_year - self.year_published
    
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book1.get_book_info())
print(f"Age of the book: {book1.get_age(2024)} years")