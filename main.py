def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  print(generate_report(text))

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  # create an array by splitting text on whitespaces
  words = text.split()
  # return length of the array
  return len(words)

def count_chars(text):
  # create a new text variable the lowercases all the characters
  lower_text = text.lower()

  # create a dictionary where the key is a unique character and the value is how many times it has occured
  count_dict = {}

  # loop through the text by character
  for char in lower_text:
    # if the character is in the dictionary, increment the value by 1
    if char in count_dict:
      count_dict[char] += 1
    # else, set value to 1 
    else:
      count_dict[char] = 1

  return count_dict

def generate_report(text):
  report = ""

  title = "--- Begin report of books/frankenstein.txt --\n"

  word_count = f"{count_words(text)} words were found in the document\n\n"

  char_count_str = ""
  char_count_dict = count_chars(text)

  for char in char_count_dict:
    char_count_str += f"The '{char}' character was found {char_count_dict[char]} times\n"
  
  end = "--- End report ---"

  report += title + word_count + char_count_str + end

  return report

main()