def is_happy(n):

    seen = set()

    while n !=0 and n not in seen:
        seen.add(n)

        n = sum(int(digit)**2 for digit in str(n))

    return n ==1


print(is_happy(n=91))