def SumSquareDif(n):
    sumOfSquares = 0
    squareOfSums = 0

    for x in range(1, n+1):
        sumOfSquares += x**2
        squareOfSums += x
    squareOfSums = squareOfSums**2

    return squareOfSums - sumOfSquares

print(SumSquareDif(100))