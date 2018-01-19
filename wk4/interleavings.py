def interleavings(a,b):
  final = []
  subInterleavings(a,b,['']*len(a+b),final,0)
  return sorted(final)
  
def subInterleavings(a,b,current,resultant,i):
  if len(a+b)==0:resultant.append(''.join(current))
  if len(a)>0:
    current[i]=a[0]
    subInterleavings(a[1:],b,current,resultant,i+1)
  if len(b)>0:
    current[i]=b[0]
    subInterleavings(a,b[1:],current,resultant,i+1)

if __name__ == '__main__':
  # Run the examples in the question.
  result = interleavings('ab', 'cd')
  print(result)
  result = interleavings('a', 'cd')
  print(result)
  print(interleavings('', ''))
  print(interleavings('abcdefgh', 'ijklm'))
  print(interleavings('abcdefghij', 'nopqrstuv'))