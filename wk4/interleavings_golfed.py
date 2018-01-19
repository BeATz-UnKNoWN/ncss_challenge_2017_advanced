l=len
def interleavings(a,b):f=[];s(a,b,['']*l(a+b),f,0);return sorted(f)
def s(a,b,c,r,i):
  if l(a+b)==0:r+=[''.join(c)]
  if l(a)>0:c[i]=a[0];s(a[1:],b,c,r,i+1)
  if l(b)>0:c[i]=b[0];s(a,b[1:],c,r,i+1)