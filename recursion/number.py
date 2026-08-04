def number(i,n):
    if i>n:
        return
    print(i,end=" ")
    number(i+1,n)

result = number(1,5)
