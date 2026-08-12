""" Optimal solution for rotating an array by one position to the right. """

def rotate_array(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

result = rotate_array([1, 2, 3, 4, 5])
print(result)