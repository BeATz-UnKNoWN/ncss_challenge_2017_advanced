i,n=input,int
l,m,d=n(i("Size: ")),n(i("Moves: ")),[(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)]
x,y=i("Knight: ").split(',')
g=[['.']*l for i in range(l)]
todo=[(n(x),n(y),0)]
g[n(x)][n(y)]='0'
while len(todo)>0:
  curr=todo.pop(0)
  a=curr[0]
  b=curr[1]
  c=curr[2]
  if c<m:
    for e in d:
      u,v=a+e[0],b+e[1]
      if 0<=u<l and 0<=v<l:
        if g[u][v]=='.':g[u][v]=str(c+1)
        todo.append((u,v,c+1))
for r in g:
  print(' '.join(r))