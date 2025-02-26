#Nested Dictionaries
d = {1:'Karnataka',2:'Tamilnadu',3:{1:'andra',2:'telangana',3:'kerala'}}
d1 = {1:'Karnataka',2:'Tamilnadu',3:'Kerala'}
print(d[3][2])

res = {}

for v in d1.values():
    res[v] = len(v)

print(res)