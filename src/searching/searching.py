def linear_search(arr, target):
    # Your code here
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):  # O(log n)

    # Your code here
    # Find midpoint element
    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (right + left) // 2
    #midpoint = len(arr) // 2
    # Compare target to midpoint element
        if arr[midpoint] == target:
            # if TARGET matches midpoint LEAVE and return index
            return midpoint
        # else
        # if TARGET less than midpoint, go left
        elif arr[midpoint] > target:
            # if TARGET greater than midpoint go right
            right = midpoint - 1
        else:
            left = midpoint + 1

    return -1  # not found
