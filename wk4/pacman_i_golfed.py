l,r=len,range
d=[(-1,0),(0,-1),(1,0),(0,1)]
m=[[c for c in x.strip()] for x in open("maze.txt")]
t=0
z=l(m[0])
p=[(x//z,x%z,m[x//z][x%z]) for x in r(l(m)*l(m[0])) if m[x//z][x%z] in 'GP']
t=[(y,x) for y,x,z in p if z=='P']
      
for g in p:
  if g[2]=='G':
    q=[[g[:2]]]
    while l(q)>0:
      c = q[0]
      if c[-1]!=t[0]:
        q.pop(0)
        for y,z in d:
          r,v=c[-1][0]+y,c[-1][1]+z
          if m[r][v]!='#' and ((r,v) not in c):q+=[c+[(r,v)]]
      else:m[g[0]][g[1]]=' ';m[c[1][0]][c[1][1]]='G';break
for r in m:print(''.join(r))