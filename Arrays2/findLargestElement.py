def findLargestElement(arr): # Simplified definition
    max_val = arr[0]
    for element in arr:     # Iterate directly over elements
        if element > max_val:
            max_val = element
    return max_val

# Input:
another_array = [5, 12, 3, 40, 7]

# Function Call:
result = findLargestElement(another_array)
print(result) # Output: 40
