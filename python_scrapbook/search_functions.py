"""
Author: Russell Gerhard
This module implements several basic searching algorithms.
"""

def find_minimum(numbers: list) -> int:
    """
    Find the index of the minimum number in a list of numbers.

    Best:     O(n) comparisons
    Average:  O(n) comparisons
    Worst:    O(n) comparisons
    Memory:   O(1)
    """
    
    min_ind = 0
    lowest = numbers[0]
    for j in range(len(numbers)-1):
        if lowest > numbers[j+1]:
            lowest = numbers[j+1]
            min_ind = j+1
    return min_ind

def sequential_search(items, target):
    """
    Find the index of a target item in a list of items.

    Args:
        items (list): A list of items.
        target (any): A target item (must implement __eq__).

    Returns:
        int: The index of the target, if in list, else -1.

    Best:     O(1) comparisons
    Average:  O(n) comparisons
    Worst:    O(n) comparisons
    Memory:   O(1)    
    """

    for i,item in enumerate(items):
        if item == target:
            return i
    return -1

def iterative_binary_search(items, target):
    """
    Iteratively find the index of a target item in a sorted, comparable list.

    Args:
        items (list): A list of items in which every item can be compared to any other.
        target (any): A target item (must implement __eq__, __lt__, __gt__)

    Return:
        int: The index of the target, if in list, else -1.

    Best:     O(1) comparisons
    Average:  O(logn) comparisons
    Worst:    O(logn) comparisons
    Memory:   O(1)
    """

    left = 0
    right = len(items)-1
    while left <= right:
        mid = (left + right) // 2
        if target < items[mid]:
            right = mid - 1
        elif target > items[mid]:
            left = mid + 1
        else:
            return mid
    return -1

def recursive_binary_search(items, target):
    """
    Call recursive binary search helper; hide extra arguments from user.

    Args:
        items (list): A list of items in which every item can be compared to any other.
        target (any): A target item (must implement __eq__, __lt__, __gt__)

    Return:
        int: The index of the target, if in list, else -1.
    """

    return recursive_binary_search_helper(items, target, 0, len(items) - 1)

def recursive_binary_search_helper(items, target, left, right):
    """
    Recursively find the index of a target item in a sorted, comparable list.
    Note: This could be implemented w/out left and right by slicing items for each
            recursive call, but that's a lot of object creation!

    Args:
        items (list): A list of items in which every item can be compared to any other.
        target (any): A target item (must implement __eq__, __lt__, __gt__)
        left (int): Left bound index of search, should be initialized to 0
        right (int): Right bound index of search, should be initialized to len(items) - 1

    Return:
        int: The index of the target, if in list, else -1.

    Best:     O(1) comparisons
    Average:  O(logn) comparisons
    Worst:    O(logn) comparisons
    Memory:   O(logn)**
    
    **Tail recursion is often optimized to iteration in modern
      compilers to save memory, therefore this would likely also
      be O(1) in practice.
    """

    # Base case
    if left > right:
        return -1

    # Recursive case
    mid = (left + right) // 2
    if target < items[(left + right) // 2]:
        return recursive_binary_search_helper(items, target, left, mid - 1)
    elif target > items[(left + right) // 2]:
        return recursive_binary_search_helper(items, target, mid + 1, right)
    else:
        return((left + right) // 2)
        
find_minimum([1,2,-3,4,-1])
##print(sequential_search([1, 2,'a', 5, 'b'], 2))
##print(recursive_binary_search([1,2,3,4,5,6], 3, 0, 5))
##print(recursive_binary_search([1,2,3,4,5,6], 6, 0, 5))
##print(recursive_binary_search([1,2,3,4,5,6], 7, 0, 5))

l = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
print(recursive_binary_search(l, 88))


