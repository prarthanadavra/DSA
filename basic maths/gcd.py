def gcd(a,b):
    gcd=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    
    return gcd

result = gcd(20,15)
print(result)