#linear search is a simple search algorithm that checks each element in the list until it finds the target value or reaches the end of the list.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1