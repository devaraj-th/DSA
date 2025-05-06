
def score_of_string(s):

    res =0


    for i in range(len(s)-1):

        res += abs(ord(s[i])-ord(s[i+1]))


    return res


stri = 'zaz'

print(score_of_string(stri))