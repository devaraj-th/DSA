def remove_occurance(s,c):

    # without using replace function

    s = list(s)
    for i in range(len(s)):
        if s[i] ==c:
            s[i]= ""

    return "".join(s)

s="geeksforgeeks"
c= "e"

print(remove_occurance(s,c))