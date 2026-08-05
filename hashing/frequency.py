"""
Brute force approach
time complexity: O(n^2)
space complexity: O(n)
"""

def frequency(arr):
    visited = [False]*len(arr)
    for i in range(len(arr)):
        if visited[i]:
            continue
        count = 0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count = count + 1
                visited[j] = True
        print(count)

result = frequency([1,1,1,2,2,3,4,5,5])
