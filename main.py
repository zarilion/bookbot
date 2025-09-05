from stats import number_of_words
from stats import number_of_characters
from stats import sort_dict
from stats import get_book_text

import sys

     

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_characters = number_of_characters(text)
    report = sort_dict(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for charentry in report:
        if charentry["char"].isalpha():
            print(f"{charentry['char']}: {charentry['count']}")
    print("============= END ===============")
main()
