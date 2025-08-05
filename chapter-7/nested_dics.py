books = {
    '1984': {
        'author': 'George Orwell',
        'publish date': '1949',
        'genre': 'Dystopian',
        'rating': 4.9
    },
    'Animal Farm': {
        'author': 'George Orwell',
        'publish date': '1945',
        'genre': 'Political Satire',
        'rating': 4.7
    },
    'Brave New World': {
        'author': 'Aldous Huxley',
        'publish date': '1932',
        'genre': 'Science Fiction',
        'rating': 4.8
    },
    'Fahrenheit 451': {
        'author': 'Ray Bradbury',
        'publish date': '1953',
        'genre': 'Dystopian',
        'rating': 4.6
    },
    'To Kill a Mockingbird': {
        'author': 'Harper Lee',
        'publish date': '1960',
        'genre': 'Classic',
        'rating': 4.9
    },
    'The Great Gatsby': {
        'author': 'F. Scott Fitzgerald',
        'publish date': '1925',
        'genre': 'Tragedy',
        'rating': 4.5
    },
    'The Catcher in the Rye': {
        'author': 'J.D. Salinger',
        'publish date': '1951',
        'genre': 'Literary Fiction',
        'rating': 4.2
    },
    'Homage to Catalonia': {
        'author': 'George Orwell',
        'publish date': '1938',
        'genre': 'Memoir',
        'rating': 4.3
    }
}


def all_books_of_author():
    num_book = 0
    for title,info in books.items():
        if info['author'] == 'George Orwell':
            print (title)

def main():
    all_books_of_author()

main()