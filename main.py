from stats import number_of_words
from stats import number_of_characters
from stats import sort_dict


def get_book_text(path):
    with open(path) as file:
        return file.read()


     

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_characters = number_of_characters(text)
    print(number_of_words(text), "words found in the document")
    print(number_of_characters(text))
    print(sort_dict(num_characters))
main()
