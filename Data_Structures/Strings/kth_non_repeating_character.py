from collections import Counter
def non_repeating_character(s,k):

    char_count = {}

    non_repeat = []

    for i in s:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i]=1


    for v in char_count:
        if char_count[v] ==1:
            non_repeat.append(v)

    if k <= len(non_repeat):
        return non_repeat[k-1]
    else:
        return None
    
    

nput = 'geeksforgeeks'
k = 3

print(non_repeating_character(nput,k))