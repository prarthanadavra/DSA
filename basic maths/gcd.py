"""
brute force approach
time complexity: O(log(min(a,b)))
space complexity: O(1)
"""

def gcd(a,b):
    gcd=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    
    return gcd

result = gcd(20,15)
print(result)

"""
Better approach
time complexity: O(log(min(a,b)))
space complexity: O(1)
"""

def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i

result = gcd(20,15)
print(result)

"""
Optimal approach
time complexity: O(log(min(a,b)))
space complexity: O(1)
"""
def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a

result = gcd(20,15)
print(result)