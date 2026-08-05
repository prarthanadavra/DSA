"""
brute force approach
time complexity: O(N)
space complexity: O(1)
"""
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    
    if count==2:
        return True
    else:
        return False

result = prime(4)
print(result)