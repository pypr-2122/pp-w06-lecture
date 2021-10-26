import numpy as np

def bubble_sort(arr):
    '''
    Sorts the list or array arr using bubble sort.

    Input: arr (list or array): the array to sort
    Output: sorted_arr (list): a copy of arr, with elements sorted in order
    '''
    # Make a copy first
    sorted_arr = arr.copy()
    counter = 1
    N = len(sorted_arr)

    # Keep looping over the list until there are no more swaps
    while True:
        # Keep track of whether we've swapped anything this time
        swapped = False

        # Compare each consecutive pair of elements
        for i in range(N-counter):
            if sorted_arr[i] > sorted_arr[i+1]:
                # Swap!
                sorted_arr[i], sorted_arr[i+1] = sorted_arr[i+1], sorted_arr[i]
                swapped = True

        # The next largest element is now at the correct place, we don't need to check it anymore
        counter += 1

        # If at this point swapped is still False, we can finish
        if not swapped:
            return sorted_arr
        

# Set up a random list of integers
n = 10000
rng = np.random.default_rng()
my_list = rng.integers(1, n+1, size=n)


# Timing
import timeit

# t = timeit.timeit("bubble_sort(my_list)", number=10, globals=globals())
# print(t/10)

import cProfile

cProfile.run("bubble_sort(my_list)")