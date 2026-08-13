"""Optimal solution to rotate an array by k places to the left.
so first we will reverse the first k elements of the array then we will reverse the remaining elements of the array and finally we will reverse the whole array.

time complexity: o(2n)
space complexity: o(1)"""

def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


result = rotate_array([1,2,3,4,5,6,6,7], 3)
print(result)


    