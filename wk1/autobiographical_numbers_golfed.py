n,o=input("Number: "),''
d=[int(x) for x in n]
for i in range(len(d)):
  c = 0
  for x in d: c+=1 if x==i else 0
  if d[i] != c: o= "not "
print(n, "is "+o+"autobiographical.")