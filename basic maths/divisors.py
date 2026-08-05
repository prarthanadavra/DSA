"""
brute force approach
time complexity: O(N)
space complexity: O(N)
"""

def divisors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

result = divisors(10)
print(result)