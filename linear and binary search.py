#linear search is a simple search algorithm that checks each element in the list until it finds the target value or reaches the end of the list.
def linear_search(arr, target):# arr is the list we want to search through, and target is the value we are looking for.
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
my_list = [5, 3, 2, 8, 1]
result = linear_search(my_list, 8)
print(f"Element found at index: {result}")

#BINARY SEARCH
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(sorted_list,5)
print(f"Element found at index: {result}")