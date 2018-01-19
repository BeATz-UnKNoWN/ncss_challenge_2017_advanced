def novowelsort(l):
  s,m=[],[(''.join(c for c in w.lower() if c not in "aeiou"),w) for w in l]
  for n,v in sorted(m): s.append(v)
  return s