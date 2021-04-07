def powerDigitSum(n):
    digit = 2**n
    digitString = str(digit)
    sum = 0
    for x in range(0, len(digitString)):
        sum += int(digitString[x])
    return sum

print("Power Digit Sum:",powerDigitSum(1000))