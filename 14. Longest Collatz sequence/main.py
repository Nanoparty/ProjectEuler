from time import time
t = time()
def chainLength(n):
    counter = 1
    while n>1:
        if n%2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n+1
            counter += 1
    if n == 1:
        return counter


longestChain = 0
largestNum = 0
for x in range(1,1000000):
    length  = chainLength(x)

    if length > longestChain:
        longestChain = length
        largestNum = x

print(largestNum,":",longestChain)
tt = time()-t
print(tt)
