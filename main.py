from stats import calculate_words
from stats import create_char_dict

def get_book_text(path):
  with open(path) as book:
    return book.read()
  

def main():
  some_book = get_book_text("/home/mimr/Projects/bookbot/books/frankenstein.txt")
  words_count = calculate_words(some_book)
  new_dict = create_char_dict(some_book)
  print(f"{words_count} words found in the document")
  print(new_dict)
  
main()
