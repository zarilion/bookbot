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
