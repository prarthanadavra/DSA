""" Optimal solution to check if an array is sorted or not 
so we just apply for loop and compare the element with the next element. if the next element is smaller than current then we return false otherwise we return true. 

time complexity: O(n) because we are applying loop to check if the array is sorted or not
space complexity: O(1) because we are not using any extra space"""

def is_sorrted(arr):
    for i in range(1, len(arr)):
        if arr[i-1]<= arr[i]:
            continue
        else:
            return False
    return True

result = is_sorrted([5, 2, 3, 4, 5])
print(result)
