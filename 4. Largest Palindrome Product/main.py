def isPalindrome(n):
    number = str(n)
    while len(number) > 1:
        lastDigit = number[len(number)-1]
        firstDigit = number[0]
        if int(firstDigit) == int(lastDigit):
            number = number[1:len(number)-1]
        else:
            return False
    return True

palindromes = list()
for x in range(100, 1000):
    for y in range(100, 1000):
        if isPalindrome(x * y):
            palindromes.append(x * y)

maxPalindrome = max(palindromes)
print("Largest Palindrome:", maxPalindrome)
