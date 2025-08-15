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

def create_sorted_list(char_dict):
  unsorted_list = []
  
  def sort_on(items):
    return items["num"]

  for char in char_dict:
    list_element = {"char": char, "num": char_dict[char]}
    unsorted_list.append(list_element)
  
  unsorted_list.sort(reverse=True, key = sort_on)
  
  return unsorted_list
