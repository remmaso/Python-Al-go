# Can you write a new algorithm in python using merge sort
# that returns the sorted arr of [5, 2, 9, 1, 7, 6]

# Here are the Steps
# Merge sort is a divide-and-conquer algorithm that works by recursively splitting the input array into smaller subarrays until they contain only one element.
# It then merges these smaller sorted subarrays to produce a final sorted array. 
# The key idea is that merging two sorted arrays is relatively easy compared to sorting an unsorted array.

# Designing the merge_sort Function:>>
# The merge_sort function takes an array arr as input and returns the sorted version of that array.
# First, we handle the base case: if the length of the array is less than or equal to 1, it is already sorted, so we return the array itself.
# Otherwise, we find the midpoint of the array using integer division (//) to divide the array into two halves.
# We recursively call merge_sort on the left and right halves to sort them.
# Finally, we merge the sorted left and right halves using the merge function.

# example

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

arr = [5, 2, 9, 1, 7, 6, 11]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# can you write a simple python function

# def add_numbers(a, b):
#     sum = a + b
#     return sum

# # Testing the add_numbers function
# num1 = 5
# num2 = 7
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")
