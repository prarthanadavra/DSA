"""
bruteforce approach:
time complexity: O(log10N + 1)
space complexity: O(1)
"""

def count_digit(n):
    count = 0
    while n >0:
        lastdigit = n%10
        n=n//10
        count = count + 1
    return count

result = count_digit(73456)
print(result)


"""
Optimized approach
time complexity: O(1)
space complexity: O(1)
"""

import math
def count_digit(n):
    cnt = int(math.log10(n)) + 1
    return cnt

result = count_digit(73)
print(result)