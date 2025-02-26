d = {1:'Hello',2:'Python',3:'Learn'}

#print the values of key
print(d[2])
#get the values
print(d.get(1))
#update the dict
d[1] = 'Hi'

#remove the key in dict # clear # pop item #del # pop

            # del(d[1])
            # val= d.pop(2)
            # print(val)

            # k,v = d.popitem()
            # print(k,v)

#print the dictionary
#print(d)

#Iterate through dict

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(f"{k}:{v}")

#using the zip function

for k,v in zip(d.keys(),d.values()):
    print(f"The key {k} and it's value {v}")

#Using the map fuinction

map_keys = map(d.get,d)

for k in map_keys:
    print(k)

