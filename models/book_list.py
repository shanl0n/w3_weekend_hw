from models.book import Book

book1 = Book("Nineteen Eighty-Four", "George Orwell", "Fiction", False)

book2 = Book("Python for Dummies", "Stef Maruch", "Educational", False)

book3 = Book("Ulysses", "James Joyce", "Modernist Novel", False)

book4 = Book("Moby Dick", "Herman Melville", "Fiction", True)


books = [book1, book2, book3, book4]

def delete_book(title):
    book_to_delete = None
    for book in books:
        if book.title == title:
            book_to_delete = book
            break
        
    books.remove(book_to_delete)