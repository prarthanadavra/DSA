"""
time complexity: O(log10N + 1)
space complexity: O(1)
"""

def palindrone(n):
    dup=n
    res=0
    while n>0:
        lastdigit = n%10
        n=n//10
        res=(res*10)+lastdigit
    if dup==res:
        return True
    else:
        return False

result = palindrone(131)
print(result)