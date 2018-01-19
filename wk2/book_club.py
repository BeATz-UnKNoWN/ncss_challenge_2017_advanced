line = input("Book read: ")
names = set()
data = {}
while line:
  book,name = line.strip().split(':')
  if name not in names:
    names.add(name)
  if book not in data:
    data[book] = [name]
  else:
    data[book].append(name)
  line = input("Book read: ")
  
for book in sorted(data.keys()):
  bookNames = set(data[book])
  diff = names-bookNames
  print(book + ":", "Everyone has read this!" if diff == set() else ", ".join(word for word in sorted(diff)))