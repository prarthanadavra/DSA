"""
Brute force approach
time complexity: O(n)
space complexity: O(1)
"""
def sum(i,n):
    sum=0
    for i in range(n+1):
        sum = sum + i
    print(sum)

result = sum(1,3)

"""
using formula
time complexity: O(1)
space complexity: O(1)
"""
def sum(n):
    return (n*(n+1))//2

result = sum(3)
print(result)

"""
Recrsive approach
time complexity: O(n)
space complexity: O(n)
"""
def sum(i,n):
    if i>n:
        return 0
    return i + sum(i+1,n)

result = sum(1,3)
print(result)