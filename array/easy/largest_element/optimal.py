""" Optimal solution to find the largest element in an array 
so for that we take the first element as largest and then we iterate through array and check if current element is greter than largest then we update the largest with current and at the end we return the largest element.

Time complexity of this approach is O(n) and space complexity is O(1)"""

def largest_element(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

result = largest_element([3,2,1,4,5,6,7,3,10,100])
print(result)