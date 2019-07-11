# Largest Contiguous Sum

# Given an array of positive and negative integers, write a function to
# find the contiguous sequence (in other words, a non-empty subarray of
# adjacent elements) with the largest sum. Return the sum.

# Sample input: [2, 3, -8, -1, 2, 4, -2, 3]
# Expected output: 7, from summing up the sequence 2, 4, -2, 3

# Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] 
# Expected output: 19, from summing up the sequence 1, 3, -2, 3, 4, 7, 2,
# -9, 6, 3, 1

# Analyze the time and space complexity of your solution.

arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] 

def largest_contig( arr ):
    largest_set = arr

    set_length = 1
    while set_length <= len(arr):
        for i in range(0, len(arr) - (set_length - 1)):
            section = slice(i, set_length + i)
            if sum(arr[section]) > sum(largest_set):
                largest_set = arr[section]
        set_length += 1

    print('LARGEST SET: ', largest_set)
    print('LARGEST SUM: ', sum(largest_set))
    return sum(largest_set)

largest_contig(arr)