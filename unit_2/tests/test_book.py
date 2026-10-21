from lib.book import *

'''
test create book
constructs fields
'''
def test_create_books_constructs_fields():
    book = Book('Emma', 'Jane Austin')
    assert book.id == 0
    assert book.title == 'Emma'
    assert book.author == 'Jane Austin'

'''
test given 2 identical books
that they are equal to each
'''
def test_books_Are_identical():
    book1 = Book('Emma', 'Jane Austin')
    book2 = Book('Emma', 'Jane Austin')

    assert book1 == book2

'''
test given a book
it returns a string nicely formatted
'''
def test_book_has_nice_string_format():
    book = Book('Emma', 'Jane Austin')
    assert str(book) == 'Book(0, Emma, Jane Austin)'