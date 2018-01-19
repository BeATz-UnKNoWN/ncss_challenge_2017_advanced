def novowelsort(the_list):
  pair_list = [(''.join(c for c in word.lower() if c not in "aeiou"), word) for word in the_list]
  pair_list.sort(key=lambda pair: pair[0])
  sorted_list = []
  for novowel, withvowel in pair_list: sorted_list.append(withvowel)
  return sorted_list

if __name__ == '__main__':
  # Example calls to your function.
  print(novowelsort(['alpha', 'beta']))
  print(novowelsort(['once', 'upon', 'abc', 'time', 'there', 'were', 'some', 'words']))