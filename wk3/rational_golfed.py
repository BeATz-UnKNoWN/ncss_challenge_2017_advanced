def g(a,b):
  while b:a,b=b,a%b
  return a
def s(a,b):
  d=g(a,b)
  return Rational(a//d,b//d)
class Rational:
  def __init__(t,n,d):
    t.n=n
    t.d=d
  def __eq__(t,o):
    a,b=s(t.n,t.d),s(o.n,o.d)
    if a.n==b.n and a.d==b.d:return True
    return False
  def __str__(t):
    i,c=0,s(t.n,t.d)
    if c.n<0:
      while -c.n>=c.d:c.n+=c.d;i-=1
    else:
      while c.n>=c.d:c.n-=c.d;i+=1
    if i<0:c.n*=-1
    return str(i) if c.n==0 else "{}{}/{}".format(str(i or ''),''.join(['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'][int(i)] if i.isdigit() else i for i in str(c.n)),''.join(['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉'][int(i)] if i.isdigit() else i for i in str(c.d)))
  def __add__(t,o):return s(t.n*o.d+o.n*t.d,t.d*o.d)
  def __mul__(t,o):return s(t.n*o.n,t.d*o.d)
  def __sub__(t,o):return s(t.n*o.d-o.n*t.d,t.d*o.d)
  def __truediv__(t,o):return s(t.n*o.d,t.d*o.n)