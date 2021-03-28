filename = 'c:/Users/nfoot/Documents/ProjectEuler/ProjectEuler/13. Large Sum/input'
array = []
f = open(filename, "r")
array = []
for line in f:
    array.append(int(line))

arraySum = sum(array)
print(str(arraySum)[:10])