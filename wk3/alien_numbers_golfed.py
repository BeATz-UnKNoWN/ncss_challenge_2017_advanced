def alien2float(string):
  t,d,n,x,f=0.0,{'a':0,'e':1,'i':2,'o':3,'u':4},[],0,False
  for c in string:
    if c in 'AEIOU':
      if f: return None
    elif c in 'aeiou':
      if not f: f = True
      x += 1
    else: return None
    n.append(d[c.lower()])
  p = x*-1
  for i in n[::-1]:t+=i*5**p;p+=1
  return t