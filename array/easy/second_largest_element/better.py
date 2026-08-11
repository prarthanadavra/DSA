"""Better approach to find the second largest element in an array.
so in first pass we find the largest element and in second pass we take second largest as -1 and then we apply loop and compare each element with second largest and also check if it is not equal to largest then we update second largest as current element.

time complexity: O(2n) because we are applying loop to find the largest and second largest element in the array
space complexity: O(1) because we are not using any extra space"""

def second_largest_element(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]

    second_largest = -1
    for i in range(len(arr)):
        if arr[i]>second_largest and arr[i]!=largest:
            second_largest = arr[i]
    return second_largest

result = second_largest_element([10, 5, 8, 12, 15])
print(result)