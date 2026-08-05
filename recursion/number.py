"""
forward recursion
time complexity: O(n)
space complexity: O(n)
"""

def number(i,n):
    if i>n:
        return
    print(i,end=" ")
    number(i+1,n)

result = number(1,5)

"""
backward recursion
time complexity: O(n)
space complexity: O(n)
"""

def number(n):
    if n==0:
        return
    number(n-1)
    print(n,end=" ")

result = number(5)
