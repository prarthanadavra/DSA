def count_digit(n):
    count = 0
    while n >0:
        lastdigit = n%10
        n=n//10
        count = count + 1
    return count

result = count_digit(7)
print(result)