def sum(i,n):
    if i>n:
        return 0
    return i + sum(i+1,n)

result = sum(1,3)
print(result)