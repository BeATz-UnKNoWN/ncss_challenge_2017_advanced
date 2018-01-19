def author_rankings(l):
  d,s={},'author'
  for t in l:
    for p in t['posts']:d[p[s]]=p['upvotes']+(d[p[s]] if p[s] in d else 0)
  return sorted([((a,d[a])+(("Insignificantly" if d[a]==0 else "Cautiously" if d[a]<20 else "Justifiably" if d[a]<100 else "Wickedly" if d[a]<500 else "Diabolically")+" Evil",)) for a in d],key=lambda t:(-t[1],t[0]))