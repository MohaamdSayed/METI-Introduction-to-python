# Example list
example_list = [38, 27, 43, 3, 9, 82, 10]

print("Original list:", example_list)

# Helper variables to hold temporary data
temp_list = example_list[:]
n = len(example_list)

# Begin merge sort
size = 1
while size < n:
    for left_start in range(0, n, 2 * size):
        mid = min(left_start + size, n)
        right_end = min(left_start + 2 * size, n)

        # Merge two halves: [left_start, mid) and [mid, right_end)
        left, right = left_start, mid
        idx = left_start

        while left < mid and right < right_end:
            if example_list[left] <= example_list[right]:
                temp_list[idx] = example_list[left]
                left += 1
            else:
                temp_list[idx] = example_list[right]
                right += 1
            idx += 1

        # Copy remaining elements of the left half
        while left < mid:
            temp_list[idx] = example_list[left]
            left += 1
            idx += 1

        # Copy remaining elements of the right half
        while right < right_end:
            temp_list[idx] = example_list[right]
            right += 1
            idx += 1

    # Copy temp_list back to example_list
    example_list[:] = temp_list[:]
    size *= 2

print("Sorted list:", example_list)