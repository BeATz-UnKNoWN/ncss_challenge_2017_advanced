def to_camel(i):
  s=i.split('_')
  i=s.pop(0)+''.join(w[0].upper()+w[1:] for w in s)
  return i