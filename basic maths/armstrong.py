def armstrong(n):
    sum=0
    dup=n
    while n>0:
        lastdigit = n%10
        n=n//10
        sum = sum + (lastdigit*lastdigit*lastdigit)
    
    if sum==dup:
        return True
    else:
        return False

result = armstrong(153)
print(result)