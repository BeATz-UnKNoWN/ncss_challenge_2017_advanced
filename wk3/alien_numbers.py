def alien2float(string):
  # TODO
  translated = 0.0
  trans = {'a':0,'e':1,'i':2,'o':3,'u':4}
  nums = []
  numOfFloat = 0
  processingFloat = False;
  for c in string:
    if c in 'AEIOU':
      if processingFloat: return None
    elif c in 'aeiou':
      if not processingFloat: processingFloat = True
      numOfFloat += 1
    else:
      return None
    nums.append(trans[c.lower()])
  power = numOfFloat*-1
  for num in nums[::-1]:
    translated += num * (5**power)
    power+=1
  return translated


if __name__ == '__main__':
  # Run the examples in the question.
  print(repr(alien2float('IU')))
  print(repr(alien2float('OUAooea')))
  print(repr(alien2float('iuAE')))