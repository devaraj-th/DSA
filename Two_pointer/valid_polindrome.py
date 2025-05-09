




def valid_polindrome(s):
    l=0
    r=len(clean_text)-1

    while l < r:
        if clean_text[l]==clean_text[r]:
            l+=1
            r-=1
        else:
            return False
            
        
    return True


        
s = " "

s_lower = s.lower()

clean_text = ''.join(char for char in s_lower if char.isalnum())
print(valid_polindrome(clean_text))