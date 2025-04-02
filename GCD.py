def GCD(a,b):
    while b:
        a,b = b, a%b
    return a # using Euclidean Algorithm
    

print(GCD(8,4))