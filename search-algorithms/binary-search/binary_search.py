"""
Binary search is a highly efficient way to find an item in a sorted list by repeatedly dividing the search area in half.
Here's how it works:
    - Start with a sorted array
    - Look at the middle element
    - If it's your target - great, you're done!
    - If your target is smaller, repeat the search in the left half
    - If your target is larger, repeat the search in the right half
    - Keep dividing until you find the element or determine it's not there
"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
numbers = [1, 3, 4, 7, 9, 13, 15, 19, 21]
result = binary_search(numbers, 7)  # Returns 3 (index of 7)
print(result)