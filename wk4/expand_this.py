from numpy.polynomial import polynomial as P
terms = input("RPN: ")
eqn=[]
pronumeral=''
for term in terms.split():
  if term.isalnum():
    if term.isalpha():eqn.append([0,1]);pronumeral=term
    else:eqn.append([int(term)])
  else:
    x,y=eqn.pop(-2),eqn.pop(-1)
    if term=='+':eqn.append(P.polyadd(x,y))
    elif term=='-':eqn.append(P.polysub(x,y))
    elif term=='*':eqn.append(P.polymul(x,y))
    elif term=='^':eqn.append(P.polypow(x,y[0]))
    
eqn=eqn[0]
output=''
for index,term in enumerate(eqn[::-1]):
  if term!=0:
    operator="" if index==0 else " + " if term>0 else " - "
    if index==0:coef = "" if (int(term)==1 and len(eqn)-1-index>0) else "-" if (int(term)==-1 and len(eqn)-1-index>0) else str(int(term))
    else:coef = "" if (int(term)==1 and len(eqn)-1-index>0) else str(abs(int(term)))
    power = '' if (len(eqn)-1-index)==0 else pronumeral if ((len(eqn)-1-index)==1) else (pronumeral+'^'+str(len(eqn)-index-1))
    output+=operator + coef + power
  elif term==0 and len(eqn)==1:output='0'
print(output)