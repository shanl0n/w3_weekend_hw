from flask import Blueprint, render_template, request

from models.book import Book
from models.book_list import *

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route('/books')
def index():
    return render_template('index.jinja', title='Book List', book_list=books)


@books_blueprint.route('/books', methods=['POST'])
def add_new_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = False
    new_book = Book(title, author, genre, checked_out)
    books.append(new_book)
    return render_template('index.jinja', title='Books Page', book_list=books)

@books_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)  
    return render_template('index.jinja', title='Books Page', book_list=books)