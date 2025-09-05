from stats import number_of_words
from stats import number_of_characters


def get_book_text(path):
    with open(path) as file:
        return file.read()


     

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(number_of_words(text), "words found in the document")
    print(number_of_characters(text))
main()
