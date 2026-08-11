"""Optimal solution to find the second largest element in an array.
so first we take first element as largest and second largest as -1 and then we apply loop to find the largest and second largest element in the array. suppose we find an element which is greater than largest then we update second largest as largest and largest as current element. if we find an element which is greater than second largest but less than largest then we update second largest as current element.

time complexity: O(n) because we are applying loop to find the largest and second largest element in the array
space complexity: O(1) because we are not using any extra space"""

def second_largest_element(arr):
    largest = arr[0]
    second_largest = -1
    for i in range(1,len(arr)):
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest = arr[i]
    return second_largest

result = second_largest_element([10, 5, 8, 12, 15])
print(result)
