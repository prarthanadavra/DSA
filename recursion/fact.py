def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

result = fact(5)
print(result)

def fact2(n):
    result = 1
    for i in range(n,0,-1):
        result = result * i
    return result

r = fact2(5)
print(r)