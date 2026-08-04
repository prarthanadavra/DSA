def reverse(n):
    res=0
    while n>0:
        lastdigit = n%10
        n=n//10
        res=(res*10)+lastdigit
    return res

result = reverse(123456789)
print(result)