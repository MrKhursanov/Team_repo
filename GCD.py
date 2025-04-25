def GCD(a,b):
    while b:
        a,b = b, a%b
    return a # using Euclidean Algorithm

print('hi, world') 

# This algorithm is pretty usefull


print(GCD(8,4))