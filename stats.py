def calculate_words(book):
  words = book.split()
  return len(words)

def create_char_dict(book):
  low_book = book.lower()
  char_dict = {}
  for char in low_book:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict