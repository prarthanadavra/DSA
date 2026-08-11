""" brute force approach to find the second largest element in an array 
again first we sort the array and then we need to apply loop to find second largest element because it is possible that the largest element appears multiple times so if we sort the array and just take second last element then it will not be correct because it is possible that the largest element appears multiple times so we need to apply loop to find second largest element 

time complexity: O(nlogn) for sorting and O(n) for loop so overall time complexity is O(nlogn + n)
space complexity: O(1) because we are not using any extra space
"""
"""brute force approach to find the largest element in an array
first sort the array in ascending order and return the last element of the array

for sorting we use quick sort algorithm so time complexity of sorting is O(nlogn) and space complexity is O(1)"""

def quick(arr,low,high):
    pivot = arr[low]
    i,j = low,high
    while i<j:
        while i<=high-1 and arr[i]<=pivot:
            i=i+1
        while j>=low+1 and arr[j]>pivot:
            j=j-1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        partition_index = quick(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
    return arr

def second_largest_element(arr):
    n = len(arr)
    sorted_arr = quick_sort(arr,0,n-1)
    largest = sorted_arr[n-1]
    for i in range(n-2,-1,-1):
        if sorted_arr[i]!=largest:
            second_largest = sorted_arr[i]
            break
    return second_largest

result = second_largest_element([64, 25, 12, 22, 11])
print(result)