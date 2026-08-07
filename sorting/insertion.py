def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    return arr

result = insertion_sort([64, 25, 12, 22, 11])
print(result)

"""
time complexity: O(n^2)
space complexity: O(1)
if array is already sorted, time complexity: O(n) which is best case scenario
"""