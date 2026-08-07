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

result = quick_sort([64, 25, 12, 22, 11],0,4)
print(result)

"""
time complexity: O(nlogn)
space complexity: O(1)"""