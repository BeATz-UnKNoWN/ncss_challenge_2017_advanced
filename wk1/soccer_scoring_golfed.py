d=[x.split() for x in open("commentary.txt")]
a,v,b=d.pop(0)
t=[l[0] for l in d]
o=sorted([(a,t.count(a)),(b,t.count(b))],key=lambda x:-x[1])
print(*o[0]);print(*o[1])