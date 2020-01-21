import random
tarr = list(range(10))
random.shuffle(tarr)
print("initial array: ", tarr)


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  # 0 
        smallest_index = cur_index # 0, changes to 1 if arr[1] is smaller than arr[0]
        # TO-DO: find next smallest element
        for el in range(i+1, len(arr)):
            # el = 1
            if arr[el] < arr[smallest_index]:
                # changes smallest_index to 1 if arr[1] is smaller than arr[0] - initial pass
                smallest_index = el
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    print("Selection sort: ", arr)
    return arr

selection_sort(tarr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for el in range(i+1, len(arr)):
            if arr[i] > arr[el]:
                arr[i], arr[el] = arr[el], arr[i]
    print("Bubble sort: ", arr)
    return arr

bubble_sort(tarr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr