# Example list
example_list = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", example_list)

n = len(example_list)
# Traverse through all elements in the list
for i in range(n):
    # Track if any swapping occurs
    swapped = False
    # Compare each pair of adjacent elements
    for j in range(0, n - i - 1):
        if example_list[j] > example_list[j + 1]:
            # Swap if the element is greater than the next
            example_list[j], example_list[j + 1] = example_list[j + 1], example_list[j]
            swapped = True
    # If no two elements were swapped, the list is already sorted
    if not swapped:
        break

print("Sorted list:", example_list)