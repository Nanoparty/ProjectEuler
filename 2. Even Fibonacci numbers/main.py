x = 1
y = 2
sum = 2
while x + y < 4000000:
    z = x + y
    if z % 2 == 0:
        sum += z
        print("Adding ", z)
    x = y
    y = z
print("Sum:", sum)