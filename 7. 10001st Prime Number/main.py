def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def nthPrime(n):
    primeCount = 0
    index = 2
    while primeCount < n:
        if isPrime(index):
            primeCount+=1
        index+=1
    return index-1

print("100th Prime:", nthPrime(10001))
