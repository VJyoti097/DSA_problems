import math

""" 
Maximum Absolute Difference

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|,
 where |x| denotes absolute value of x.

"""

#Brute forsce solution:-

def max_abs_diff(arr):
    max_absolute_diff = -math.inf
    for i in range(len(arr)):
        for j in range(len(arr)):
            absolute_diff = abs(arr[i] - arr[j]) + abs(i-j)
            if max_absolute_diff < absolute_diff:
                max_absolute_diff = absolute_diff
    return max_absolute_diff

# print(max_abs_diff([1, 3, -1]))

#Time Complexity = O(n2)
#Space Complexity = (1)

#for optimal approach

#Observation:-
    # i,j = j,i and absolute difference is 0
    #   -->So, will take f(i, j) > f(j,i)

def max_abs_diff_optimal(arr):
    x_max = -math.inf
    x_min = math.inf
    y_max = -math.inf
    y_min = math.inf

    for i in range(len(arr)):
        x = arr[i] + i
        y = arr[i] - i
        if x_max < x:
            x_max = x
        if x_min > x:
            x_min = x
        if y_max < y:
            y_max = y
        if y_min > y:
            y_min = y
    return max((x_max-x_min), (y_max - y_min))

print(max_abs_diff_optimal([1, 3, -1]))

#time COmplexity is O(n)
#spcae compexity is O(1)
