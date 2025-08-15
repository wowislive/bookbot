import sys
from stats import calculate_words
from stats import create_char_dict
from stats import create_sorted_list

def get_book_text(path):
  with open(path) as book:
    return book.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
  some_book = get_book_text(sys.argv[1])
  words_count = calculate_words(some_book)
  new_dict = create_char_dict(some_book)
  sorted_list = create_sorted_list(new_dict)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  for char in sorted_list:
    if char["char"].isalpha():
      print(f"{char["char"]}: {char["num"]}")      
  print("============= END ===============")
  
main()
