stuff = input("Enter number: ")
imei = [int(x) for x in stuff]
imei.reverse()
total = 0
for i in range(0, len(imei)):
    if i % 2 == 1:
        num = [int(x) for x in str(imei[i] * 2)]
        for j in range(0, len(num)):
            total += num[j]
    else:
        total += imei[i]
        
if total % 10 == 0:
    print("Valid.")
else:
    print("Invalid.")