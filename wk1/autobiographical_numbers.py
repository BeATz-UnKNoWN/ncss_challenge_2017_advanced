numStr = input("Number: ")
digits = [int(x) for x in numStr]
output = "is autobiographical."
for i in range(len(digits)):
    digitCount = 0
    for digit in digits:
        if digit == i:
            digitCount += 1
    if digits[i] != digitCount:
        output = "is not autobiographical."
        break
print(numStr, output)