# {{TABLE NAME}} Model and Repository Classes Design Recipe


As a user 
I want to be able to see a books title and author

As a user
I want to list all the books of the books table 
to see the titles and the authors

## 1. Design and create the Table

Already designed in the seeds


## 2. Create Test SQL seeds

Already done in the seeds

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python

# Table name: books


class Book:
    pass

class BookRepository
pass

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Book:
    def __init__(self, title, author, id = 0):
        self.id = id
        self.title = title
        self.author = author
```

## 5. Define the Repository Class interface

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class BookRepository():

    def __init__(self, connection):
        self._connection = connection


    def all():
        # Parameters:
        #   None
        # Side-Effects:
        #   None
        # Returns:
        #   Returns an array of Student objects.

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python

```
test create book
constructs fields
```
def test_create_books_constructs_fields():
    book = Book('Emma', 'Jane Austin')
    assert book.id == 0
    assert book.title == 'Emma'
    assert book.author = 'Jane Austin'

```
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
        Book(1, 'Nineteen-Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

