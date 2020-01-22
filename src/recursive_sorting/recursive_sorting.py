import random
# TO-DO: complete the helper function below to merge 2 sorted arrays

list1 = list(range(5))
random.shuffle(list1)
# print("*ORIGINAL list1*", list1)

list2 = list(range(10))
random.shuffle(list2)
# print("**ORIGINAL list2**", list2)


# def merge( arrA, arrB ):
#     # elements = len( arrA ) + len( arrB )
#     # merged_arr = [0] * elements
#     merged_arr = []
#     # TO-DO
#     j = 0
#     k = 0 
#     while j < len(arrA) and k < len(arrB):
#         if arrA[j] < arrB[k]:
#             merged_arr.append(arrA[j])  
#             j += 1
#         else: 
#             merged_arr.append(arrB[k])
#             k += 1
#     merged_arr += arrA[j:]
#     merged_arr += arrB[k:]
#     print("MERGED: ", merged_arr)
#     return merged_arr


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    j = 0
    k = 0 
    for i in range(0, elements):
        print("i",i, "j", j, "k", k)
        if j >= len(arrA):
            print("testing")
            merged_arr[i] = arrB[k]
            k += 1

        elif k >= len(arrB):
            print("testing2")            
            merged_arr[i] = arrA[j]
            j += 1

        elif arrA[j] < arrB[k]:
            print("testing3")
            merged_arr[i] = arrA[j]
            j += 1

        else:
            print("testing4")
            merged_arr[i] = arrB[k]
            k += 1

    print("MERGED: ", merged_arr)
    return merged_arr

print("merging...", merge([0,1,2], [4,5,9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    # while arr
    larr = merge_sort(arr[:middle])
    rarr = merge_sort(arr[middle:])
    # print("left", larr)
    # print("right", rarr)
    # print(merge(larr, rarr))
    return merge(larr, rarr)

# merge_sort(list1)
# merge_sort(list2)

# merge(list1, list2) 

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr



# list.extend() may be of use here.