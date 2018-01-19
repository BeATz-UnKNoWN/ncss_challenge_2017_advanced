def to_camel(ident):
  asList = list(ident)
  i = 0
  while i < len(asList):
    if asList[i] == '_':
      asList[i+1] = asList[i+1].upper()
      asList.pop(i)
      i -= 1
    i += 1
  ident = "".join(asList)
return ident


if __name__ == '__main__':
  # Run the example inputs in the question.
  print(to_camel('foo'))
  print(to_camel('raw_input'))
  print(to_camel('num2words'))
  print(to_camel('num_to_SMS'))