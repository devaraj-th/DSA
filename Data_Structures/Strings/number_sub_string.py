def number_of_substring(s1,s2):

    ans =0

    for i in range(len(s1)):
        s3 = ''

        for j in range(i,len(s1)):
            s3 +=s1[j]

            if s2.find(s3) != -1:
                ans+=1

    return ans

s1 = 'aab'
s2 = 'aaaab'

print(number_of_substring(s1,s2))