import numpy as np
from numpy.lib.histograms import _histogram_dispatcher
#Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        pos = i
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                pos = j
        arr[i], arr[pos] = min, arr[i]
    return arr


#Insertion Sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]

        j = i-1
        while j >=0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr


#Merge Sort
def merge_sort(arr:list) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

#Quick Sort
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high] 
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

#Heap Sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heap_sort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

#Non-comparison Sort
# These only work with integers in a certain range, this is specific to this type since it takes into account
#  how integers are stored in the computer. Some examples are:

#   - Counting Sort
#       -- https://brilliant.org/wiki/counting-sort/
#       -- https://www.cs.usfca.edu/~galles/visualization/CountingSort.html
#   - Radix Sort
#       -- https://brilliant.org/wiki/radix-sort/
#       -- https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
#   - Bucket Sort


#Sorting Interview Problem:
#1 - Sort 10 schools around your house by distance:
    # Probably utilize Insertion Sort, due to little amount of data and, since it sorts in place, space complexity is O(1)
#2 - eBay sorts listings by the current Bid amount:
    # Non-comparative methods since data is long and numbers are always between a certain range
#3 - Sport scores on ESPN:
    # If scores are only integers then we can utilize non-comparative methods since scores are very limited in value (almost never)
    # exceed 100. Since there are multiple sports quicksort might be best.
#4 - Massive database (can't fit all into memory) needs to sort through past year's user data
    # Merge Sort, this will allow us to parcel problem into pieces form the beginning and tackle in parts
#5 - Almost sorted Udemy review data needs to update and add 2 new reviews
    # Insertion Sort since data is almost sorted and not many new entries will exist.
#6 - Temperature Records for the past 50 years in Canada
    # Non-comparative sort if there are no decimal places, else we cna use quicksort to save on the space complexity.
#7 - Large user name database needs to be sorted. Data is very random.
    # Quick sort or Merge sort since the data is very random and there are no repeated values. If there is enough memory 
    # merge sort might be best since it eliminates the worst case scenario of O(n^2) of quick sort.
#8 - You want to teach sorting for the first time
    # Bubble sort

if __name__ == "__main__":
    np.random.seed(2020)
    print("Bubble Sort:")
    arr = np.random.randint(100, size=10)
    print(arr)
    print(bubble_sort(arr))
    
    print("\nSelection Sort:")
    arr = np.random.randint(100, size=10)
    print(arr)
    print(selection_sort(arr))

    print("\nInsertion Sort:")
    arr = np.random.randint(100, size=10)
    print(arr)
    print(insertion_sort(arr))


    print("\nMerge Sort:")
    #For some reason does not work with np array.
    arr = list(np.random.randint(100, size=10))
    print(arr)
    merge_sort(arr)
    print(arr)

    print("\nQuick Sort:")
    #For some reason does not work with np array.
    arr = list(np.random.randint(100, size=10))
    print(arr)
    quick_sort(arr, 0, len(arr)-1)
    print(arr)