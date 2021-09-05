"""
CHANGED DOCSTRING COMMENT
This module implements several basic sorting algorithms.

There are five general classes of comparison sorting algorithms:
Selection: selection sort and heapsort
Insertion: insertion sort and tree sort
Exchange: bubble sort and quicksort
Merge: merge sort
"""

def swap(l: list, i: int, j: int) -> None:
    """Exchange the items at two positions in a list."""
    # Equivalently, list[i], list[j] = list[j], list[i]
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def selection_sort(l: list, trace: bool = True):
    """
    On each iteration i starting at 0, find the minimum of the remaining list
    from i to the end and swap it with the value at index i.

    Best:     O(n**2) comparisons, O(1) swaps
    Average:  O(n**2) comparisons, O(n) swaps
    Worst:    O(n**2) comparisons, O(n) swaps
    Memory:   O(1)
    Stable:   No
    Online:   No
    Adaptive: No
    Parallel: Not really
    Method:   Selection

    This sort is easy to understand and implement.
    """
    i = 0
    while i < len(l) - 1:
        min_index = i
        j = i + 1
        while j < len(l):
            if l[j] < l[min_index]:
                min_index = j
            j += 1
        # Swap does not preserve stability
        if min_index != i:
            swap(l, i, min_index)
        i += 1
    if trace:
        print(l)

def selection_sort_with_insertion(l: list, trace: bool = True):
    """
    On each iteration i starting at 0, find the minimum of the remaining list
    from i to the end and insert it at index i.

    Best:     O(n**2) comparisons, O(1)    swaps
    Average:  O(n**2) comparisons, O(n**2) swaps
    Worse:    O(n**2) comparisons, O(n**2) swaps
    Memory:   O(1)
    Stable:   Yes
    Online:   No
    Adaptive: No
    Parallel: Not really
    Method:   Selection and Insertion

    This sort is easy to understand and implement. It uses a linear-time
    insertion step instead of a constant-time swap to make the sort stable. This
    increases the order of complexity of the number of swaps performed.
    """
    i = 0
    while i < len(l) - 1:
        min_index = i
        j = i + 1
        while j < len(l):
            if l[j] < l[min_index]:
                min_index = j
            j += 1

        # Little bit of insertion code to preserve stability
        save = l[min_index]
        while min_index > i:
            l[min_index] = l[min_index - 1]
            min_index -= 1
        
        l[i] = save
        i += 1
    if trace:
        print(l)

def bubble_sort(l: list, trace: bool = True, online: bool = False) -> None:
    """
    On each iteration i starting at 0, make a pass through the list up to
    position -i, exchanging any two values if they are out of order. Each
    iteration, check to see if any swaps were performed.

    Best:     O(n)    comparisons, O(1)    swaps
    Average:  O(n**2) comparisons, O(n**2) swaps
    Worst:    O(n**2) comparisons, O(n**2) swaps
    Memory:   O(1)
    Stable:   Yes
    Online:   Yes
    Adaptive: Yes
    Parallel: Odd-even transposition
    Method:   Exchange

    This sort is easy to understand and implement. Checking for swaps makes it
    adaptive, so it performs better on friendlier data. I believe it is online
    because I could prepend values and bubble them, or I could implement it with
    lower values sinking and append new data.
    """
    n = len(l)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if l[j + 1] < l[j]:
                swapped = True
                swap(l, j, j + 1)
        if swapped == False:
            break
        
    # Test online capability
    if online:
        data = input("New data: ")
        while data:
            data = float(data)
            l.insert(0, data) # linear
            for j in range(len(l) - 1):
                if l[j + 1] < l[j]:
                    swap(l, j, j + 1)

            print(l)
            data = input("New data: ")
        
    if trace:
        print(l)

def insertion_sort(l: list, trace: bool = True, online: bool = False) -> None:
    """
    On each iteration i starting at 1, insert the correct item to position i - 1
    among the first i + 1 items.

    Best:     O(n)    comparisons, O(1)    swaps
    Average:  O(n**2) comparisons, O(n**2) swaps
    Worst:    O(n**2) comparisons, O(n**2) swaps
    Memory:   O(1)
    Stable:   Yes
    Online:   Yes
    Adaptive: Yes
    Parallel: Not really
    Method:   Insertion
    """
    for i in range(1, len(l)):
        current_item = l[i]
        j = i - 1
        while j > -1:
            if l[j] > current_item:
                l[j + 1] = l[j]
                j -= 1
            # since items before current are sorted, no need to look back further
            else:
                break
        if i != j + 1:
            l[j + 1] = current_item

    # Test online capability
    if online:
        data = input("New data: ")
        while data:
            data = float(data)
            l.append(data)
            current_item = data
            j = len(l) - 2
            while j > -1:
                if l[j] > current_item:
                    l[j + 1] = l[j]
                    j -= 1
                else:
                    break
        
            if i != j + 1:
                l[j + 1] = data

            print(l)
            data = input("New data: ")
        
    if trace:
        print(l)

def quick_sort(l: list, trace: bool = True) -> None:
    """
    Call helper function to hide left and right parameters.
    See quick_sort_helper documentation for algorithm details.
    """

    quick_sort_helper(l, 0, len(l))
    

def quick_sort_helper(l: list, left: int, right: int) -> None:
    """
    Partition current list and recursively call quicksort to partition
    sublists to left and right of the pivot.

    Best:     O(n*logn) comparisons, O(n*logn) swaps
    Average:  O(n*logn) comparisons, O(n*logn) swaps
    Worst:    O(n**2) comparisons, O(n**2) swaps
    Memory:   Best: O(logn), Worst: O(n)
    Best:     O(logn)
    Average:  O(logn)
    Worst:    O(n**2)
    Stable:   No
    Online:   No
    Adaptive: No
    Parallel: Yes
    Method:   Exchange
    """
    if left < right:
        pivot_loc = partition(l, left, right)
        quick_sort_helper(l, pivot_loc + 1, right)
        quick_sort_helper(l, left, pivot_loc - 1)

def partition(l: list, left: int, right: int) -> int:
    """
    Iterate over a sublist, partitioning it into a section that is less than a
    chosen value, the pivot, or greater than that value.

    Best:     O(n) comparisons, O(1) swaps
    Average:  O(n) comparisons, O(n) swaps
    Worst:    O(n) comparisons, O(n) swaps
    Memory:   O(1)
    """

    # Establish midpoint, pivot, swap them, and est. boundary
    mid = (left + right) // 2
    pivot = l[mid]
    swap(l, mid, right)
    boundary = left

    # Iterate over the sublist
    for i in range(left, right):
        if l[i] < pivot:
            # Swap value smaller than pivot with boundary, increase boundary
            swap(l, i, boundary)
            boundary += 1

    # Put pivot back in the middle
    swap(l, boundary, right)
    return boundary
    
        
if __name__ == "__main__":
    from sort_functions import *
    l1 = [6,-4,5,4,-1,3,2,1]
    l2 = [6,-4,5,4,-1,3,2,1]
    l3 = [1,3,2,4,5]
    l4 = [1,3,2,4,5]
