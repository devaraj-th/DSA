from collections import Counter
def second_most_frequent(arr):

    freq = Counter(arr)

    freq_values= sorted(freq.values(), reverse=True)
    second_most = freq_values[1]

    for s,v in freq.items():
        if v == second_most:
            return s
        
Input = {"aaa", "bbb", "ccc", "bbb", 
         "aaa", "aaa"}

print(second_most_frequent(Input))



