import string
def countWordLengths(txt):
  arr=[0]*45
  for word in [w.strip(string.punctuation) for line in open(txt) for w in line.strip().split()]:
    if len(word) > 0:
      arr[len(word)-1]+=1
  return arr
def sim(a,b):
  numerator=denominator1=denominator2=0
  for i in range(len(a)):
    numerator+=(a[i]*b[i])
    denominator1+=a[i]**2
    denominator2+=b[i]**2
  return (numerator/((denominator1**(1/2))*(denominator2**(1/2))))
texts = [l.strip() for l in open("texts.txt")]
u=countWordLengths("unknown.txt")
results=[]
for text in texts:
  a=countWordLengths(text)
  results+=[(sim(a,u),text)]
for similarity,text in sorted(results,key=lambda x: -x[0]):print(similarity,text)