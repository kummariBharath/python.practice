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