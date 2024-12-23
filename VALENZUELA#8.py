class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book = Book("IsangKaibigan", "SarahDuts")
print(f"Book: {book.title}")
print(f"Author:{book.author}")
print(f"Book Without Author: {book.title}, {book.author}")
del (book.author)
print(book.author)