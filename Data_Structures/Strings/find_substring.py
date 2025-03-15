def sub_string(s):

    sub_string =[]

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub_string.append(s[i:j])

    return sub_string


s = 'abc'

print(sub_string(s))