
def contains_duplicate(arr):

    # result = set()

    # for i in arr:

    #     if i in result:
    #         return True
    #     else:
    #         result.add(i)

    # return False

    return len(set(arr)) != len(arr)

# nums = [1,1,1,3,3,4,3,2,4,2]

nums = [1,2,3,4]

print(contains_duplicate(nums))