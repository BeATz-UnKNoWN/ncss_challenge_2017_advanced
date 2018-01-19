import random

def generate_sentence(start_token, filenames):
  bigram = {}
  #build the bigram
  for filename in filenames:
    words = [word.lower() for line in open(filename, 'r') for word in line.split()]
    for i in range(len(words)-1):
      if words[i] in bigram:
        bigram[words[i]].append(words[i+1])
      else:
        bigram[words[i]] = [words[i+1]]
  #sentence generation
  token = start_token.lower()
  sentence = token
  length = 1
  while token != '.' and token in bigram.keys() and length < 200:
    token = random.choice(bigram[token])
    sentence += " " + token
    length += 1
  return sentence

if __name__ == '__main__':
  # The random number generator is initialised to zero here purely
  # for your own testing so that each time you run your code during
  # development, you will get the same output. Remove this to get 
  # different output each time you run your code with the same input.
  random.seed(0)
  
  # Run the examples in the question.
  for i in range(4):
    print(generate_sentence('There', ['single.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('the', ['jab.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('It', ['dracula.txt', 'pandp.txt']))
  print('=' * 80)
  for i in range(10):
    print(generate_sentence('Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))