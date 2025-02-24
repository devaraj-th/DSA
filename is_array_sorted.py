def is_array_sorted(arr):

    if len(arr) ==1:
        return True
    
    return arr[0] <= arr[1] and is_array_sorted(arr[1:])

a = [127,20,246,277,321,454,534,565,933]

print(is_array_sorted(a))