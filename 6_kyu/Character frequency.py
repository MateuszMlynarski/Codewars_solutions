def letter_frequency(text):
  lower_text = [letter.lower() for letter in text]
  letters = list(set([letter.lower() for letter in text if letter.isalpha()]))
  count_letters = [ (letter, lower_text.count(letter)) for letter in letters]
  count_letters = sorted(count_letters, key=lambda tup: (-tup[1], tup[0]))
  return count_letters

# Best practice
# from collections import Counter
# from operator import itemgetter
#
# def letter_frequency(text):
#     items = Counter(c for c in text.lower() if c.isalpha()).items()
#     return sorted(
#         sorted(items, key=itemgetter(0)),
#         key=itemgetter(1),
#         reverse=True
#     )