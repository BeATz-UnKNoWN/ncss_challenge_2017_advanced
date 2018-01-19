def author_rankings(thread_list):
  authors = {}
  results = []
  #load data into authors dict
  for thread in thread_list:
    for post in thread['posts']:
      author = post['author']
      if author in authors:
        authors[author] += post['upvotes']
      else:
        authors[author] = post['upvotes']
  #build the tuples
  for author in authors:
    u = authors[author]
    tup = (author, u)
    tup = tup[:2] + (("Insignificantly Evil" if u==0 else "Cautiously Evil" if u<20 else "Justifiably Evil" if u<100 else "Wickedly Evil" if u<500 else "Diabolically Evil"),)
    results.append(tup)
  results.sort(key=lambda tup: (-tup[1], tup[0]))
  return results


if __name__ == '__main__':
  # Example calls to your function.
  print(author_rankings([
    {
        'title': 'Invade Manhatten, anyone?',
        'tags': ['world-domination', 'hangout'],
        'posts': [
            {
                'author': 'Mr. Sinister',
                'content': "I'm thinking 9 pm?",
                'upvotes': 2,
            },
            {
                'author': 'Mystique',
                'content': "Sounds fun!",
                'upvotes': 0,
            },
            {
                'author': 'Magneto',
                'content': "I'm in!",
                'upvotes': 0,
            },
        ],
    }
  ]))
