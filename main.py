# The arr contains random numbers that are unsorted
# We need to find the maximum number in it.
# Assume that the first element of the arr is the maximum number


arr = [5, 4, 8, 7, 2]

# We are assuming that the first element of the arr is maximum number
max_num = arr[0]


for i in arr:
    if i > max_num:     # Check each element and compare
        max_num = i     # During loop, if an element is found larger then the max_num variable will be updated


print(max_num)