def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    if a == 0 or b == 0:
        return 0
    lcm = (a * b) / GCD(a,b)
    return lcm

def recurse(input):
    result = input[1]
    if len(input) > 2:
        result = recurse(input[1:])
    print(input, ":",result)
    return LCM(input[0], result)

input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print("LCM:",recurse(input))


    