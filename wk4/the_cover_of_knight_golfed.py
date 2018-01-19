i,n=input,int
l,m,d=n(i("Size: ")),n(i("Moves: ")),[(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)]
x,y=i("Knight: ").split(',')
def p(g,x,y,t):
  if g[x][y]=='.' or m+1-t<n(g[x][y]):g[x][y]=str(m-t)
  if t>0:
    for e in d:
      a,b=x+e[0],y+e[1]
      if 0<=a<l and 0<=b<l:p(g,a,b,t-1)
g=[['.']*l for i in range(l)]
p(g,n(x),n(y),m)
for r in g:
  print(' '.join(r))