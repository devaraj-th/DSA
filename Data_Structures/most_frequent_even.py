nums = [4,4,4,9,2,4]

nums.sort()

num_dict = {i:nums.count(i) for i in nums if i%2==0}

if len(num_dict) ==0:
    print(-1)
else:
    d = max(num_dict, key=lambda k:num_dict[k])

    print(d)