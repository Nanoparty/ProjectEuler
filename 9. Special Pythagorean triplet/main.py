#c = 1000 - a - b
#c^2 = a^2 + b^2 

# (1000 - a - b)^2 = a^2 + b^2
#a^2 + 2ab - 2000a + b^2 -2000b + 1000000 = a^2 + b^2
#2ab - 2000a - 2000b = -1000000

def pythagTriplet(sum):
    for a in range(1, int(sum/3)):
        for b in range(1 , int(sum/2)):
            c = sum - a - b
            if a**2 + b**2 == c**2:
                return (a*b*c)

print("Pythag:",pythagTriplet(1000))