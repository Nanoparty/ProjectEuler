def latticePath(rows, cols):
    matrix = [[0 for x in range(cols+1)] for y in range(rows+1)] 
    for x in range(0, cols+1):
        for y in range(0, rows+1):
            if x == 0:
                matrix[x][y] = 1
            elif y == 0:
                matrix[x][y] = 1
            else:
                total = 0
                total += matrix[x-1][y]
                total+= matrix[x][y-1]
                matrix[x][y] = total
            print("step:",x,":",y,":",matrix[x][y])
    return matrix[cols][rows]

print("Paths:",latticePath(20,20))

