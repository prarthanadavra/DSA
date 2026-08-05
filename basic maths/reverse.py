
"""
time complexity: O(log10N)
space complexity: O(1)
"""

def reverse(n):
    res=0
    while n>0:
        lastdigit = n%10
        n=n//10
        res=(res*10)+lastdigit
    return res

result = reverse(10400)
print(result)