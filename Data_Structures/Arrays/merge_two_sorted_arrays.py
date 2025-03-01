def merge_two_arrays(lst1,lst2):

    final_array = lst1 + lst2

    return sorted(final_array)


l1 = [1,4,8,9,10]
l2 = [2,3,5,6]

print(merge_two_arrays(l1,l2))