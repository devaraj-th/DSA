def is_binary(s):

    for char in s:
        if char !='0' and char !='1':
            return False
    return True


s='101101'
s1 = 'ge0978'
print(is_binary(s))
print(is_binary(s1))

