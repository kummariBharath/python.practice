#binary search
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

#bisection method
def bisection_method(number, tol=1e-7, max_iter=1000):
    if number<0:
        raise ValueError('square of zero is not in real numbers')
    if number==0 or number==1:
        print(f"The squareroot of {number} is {number}")
        return number
    if number<1:
        low=number
        high=1
    else:
        low=1
        high=number
    iterations=0
    while (high-low)>tol and iterations<max_iter:
        mid=(low+high)/2
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

#QUICK SORT ALGORITHM
def quick_sort(arr):
    # Base case: if list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose pivot (first element)
    pivot = arr[0]

    # Partition the list
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort and concatenate
    return quick_sort(less) + equal + quick_sort(greater)
 
if __name__ == '__main__':
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [int(x) for x in user_input.split()]
        print('Unsorted array: ')
        print(numbers)
        sorted_numbers = quick_sort(numbers)
        print('Sorted array (Quick Sort): ')
        print(sorted_numbers)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except ValueError:
        print("\nInvalid input. Please enter valid integers separated by spaces.")


#SELECTION SORT ALGORITHM
def selection_sort(items):
    n = len(items)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i] 

    return items 
    
#luhn Algorithm 
def verify_card_number(card_number):
    card_number=card_number.replace(' ','').replace('-','')
    digits=[int(d) for d in card_number][::-1]
    total=0
    for i in range(len(digits)):
        num = digits[i]
        if i%2==1:
            num*=2
            if num>9:
                num-=9
        total+=num        
    if total % 10 == 0:
        return "Valid!"
    else:
        return "Invalid"

if __name__ == "__main__":
    user_input = input("Enter a credit card number to verify: ")
    print(verify_card_number(user_input))
