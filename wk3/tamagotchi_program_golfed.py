from tamagotchi import Tamagotchi
def p(o):print(o)
d,o,i={},"No Tamagotchi with that name.",input("Command: ")
while i:
  c,x=i.split(),False
  if c[0]=="create":
    if c[1] in d:
      if d[c[1]].is_dead():d[c[1]]=Tamagotchi(c[1])
      else:p("You already have a Tamagotchi called that.");x=True
    else:d[c[1]]=Tamagotchi(c[1])
  elif c[0]=="feed":
    if c[1] not in d:p(o);x=True
    else:d[c[1]].feed()
  elif c[0]=="play":
    if c[1] not in d:p(o);x=True
    else: d[c[1]].play()
  elif c[0]!="wait":p("Invalid command.");i=input("Command: ");continue
  if not x:
    for t in sorted(d):p(d[t]);d[t].increment_time()
  i=input("Command: ")