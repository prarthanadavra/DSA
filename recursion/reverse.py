"""
forward recursion
time complexity: O(n)  
space complexity: O(n)
"""
def reverse(n):
    if n==0:
        return
    print(n,end=" ")
    reverse(n-1)

result = reverse(5)

"""
backward recursion
time complexity: O(n)
space complexity: O(n)
"""

def reverse(i,n):
    if i>n:
        return
    reverse(i+1,n)
    print(i,end=" ")

result = reverse(1,5)