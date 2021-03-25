def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def sumPrimesBelow(n):
    sum = 0
    for x in range(2, n):
        if isPrime(x):
            sum+=x
            print("prime:",x)
    return sum

print(sumPrimesBelow(10))