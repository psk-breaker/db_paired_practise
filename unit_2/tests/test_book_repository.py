from lib.book_repository import *

'''
given a book repo
test that a connection is stored
'''
def test_book_repo_can_store_a_connection(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repo = BookRepository(db_connection)
    assert repo._connection == db_connection

'''
given a repo full of books
we can see the full list of titles and authors
'''
def test_repo_can_return_all_title_and_author(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repo = BookRepository(db_connection)

    assert repo.all() == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
