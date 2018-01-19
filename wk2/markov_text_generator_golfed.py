def generate_sentence(x, n):
  b={}
  for f in n:
    w=[t.lower() for l in open(f,'r') for t in l.split()]
    for i in range(len(w)-1):b[w[i]] = b[w[i]]+[w[i+1]] if w[i] in b else [w[i+1]]
  t=x.lower()
  s,l=t,1
  while t != '.' and t in b and l < 200:
    t=random.choice(b[t])
    s+=" "+t
    l+=1
  return s