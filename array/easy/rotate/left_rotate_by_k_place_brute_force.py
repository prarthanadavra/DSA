"""Brute force solution for rotating an array by k positions to the left.
so first we will store the first k elements in a temporary array and then we will shift the remaining elements to the left and finally we will copy the temporary array to the end of the original array.

Note: so by k positions to the left means that we will move the first k elements to the end of the array and shift the remaining elements to the left. example: if we have an array [1, 2, 3, 4, 5] and we want to rotate it by 2 positions to the left then the output will be [3, 4, 5, 1, 2]

so suppose k is 5 and the length of the array is 5 then we will rotate the array by 0 positions to the left because rotating an array by its length will give us the same array. so we will take k modulo length of the array to avoid this case.

time complexity: O(n+k)
space complexity: O(k)"""

def left_rotate_array(arr, k):
    n = len(arr)
    k= k%n
    temp = arr[:k]
    for i in range(k):
        temp[i] = arr[i]
    for i in range(k,n):
        arr[i-k] = arr[i]
    j=0
    for i in range(n-k,n):
        arr[i] = temp[j]
        j= j+1
    return arr

result = left_rotate_array([1,2,3,4,5,5,6,7,8,9,1,2,3,4,], 4)
print(result)