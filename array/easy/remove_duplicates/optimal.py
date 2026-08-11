""" Optimal solution to remove duplicates from a sorted array. so for that we use two pointer approach. so if the current element is not equal to the next element then we will replace the next element with the current element and increment the index.

time complexity: O(n)
space complexity: O(1)"""

def remove_duplicates(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i = i+1
    return arr[:i+1]

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)