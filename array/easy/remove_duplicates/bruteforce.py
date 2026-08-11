""" Brute force solution to remove duplicates from a sorted array. so for that we use set data structure to store unique elements and then convert it back to a list. 
"""
def remove_duplicates(arr):
    unique_elements = set()
    for i in arr:
        unique_elements.add(i)
    index = 0
    for i in unique_elements:
        arr[index] = i
        index += 1
    return arr[:index]

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)