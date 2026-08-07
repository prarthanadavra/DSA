def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

result = bubble_sort([64, 25, 12, 22, 11])
print(result)

"""
time complexity: O(n^2)
space complexity: O(1)

if array is already sorted, time complexity: O(n) which is best case scenario
"""