a,t=input("Enter number: ")[::-1],0
for i in range(len(a)): t+=sum(int(x) for x in str(int(a[i])*2)) if i%2 else int(a[i])
print("Invalid.") if t%10 else print("Valid.")