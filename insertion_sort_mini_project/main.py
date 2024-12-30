# Example list
example_list = [12, 11, 13, 5, 6]

print("Original list:", example_list)

# Perform insertion sort
n = len(example_list)
for i in range(1, n):
    key = example_list[i]
    j = i - 1
    # Move elements of example_list[0..i-1] that are greater than key
    # to one position ahead of their current position
    while j >= 0 and example_list[j] > key:
        example_list[j + 1] = example_list[j]
        j -= 1
    # Place the key at the correct position
    example_list[j + 1] = key

print("Sorted list:", example_list)