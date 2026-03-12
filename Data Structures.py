#binary search
from ast import Raise


def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target,f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))

#Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

#bisection method
def bisection_method(number, tol=1e-7, max_iter=1000):
    if number<0:
        raise ValueError('square of zero is not in real numbers')
    if number==0 or number==1:
        print(f"The squareroot of {number} is {number}")
    if number<1:
        low=number
        high=1
    if number>1:
        low=1
        high=number
    itertions=0
    while (high-low)>tol and itertions<max_iter:
        mid=low+high/2
        if mid*mid>number:
            high=mid
        else:
            low=mid
            iterations += 1

    if iterations == max_iter:
        print(f"Failed to converge within {max_iter} iterations")
        return None

    root = (low + high) / 2
    print(f"The square root of {number} is approximately {root}")
    return root   
 
 #MERGE SORT ALGORITHM
def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [int(x) for x in user_input.split()]
        print('Unsorted array: ')
        print(numbers)
        merge_sort(numbers)
        print('Sorted array: ')
        print(numbers)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except ValueError:
        print("\nInvalid input. Please enter valid integers separated by spaces.")
