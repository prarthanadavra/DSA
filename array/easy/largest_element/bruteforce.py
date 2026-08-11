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

def largest_element(arr):
    n = len(arr)
    sorted_arr = quick_sort(arr,0,n-1)
    return sorted_arr[n-1]

result = largest_element([64, 25, 12, 22, 11])
print(result)
