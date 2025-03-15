def count_sub_string(s,t):

    count =0

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j]==t:
                count+=1

    return count


s1 = 'aab'
s2 = 'aaaab'

print(count_sub_string(s2,s1))