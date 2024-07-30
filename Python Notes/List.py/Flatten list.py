list = [2,3,4,[9,7,5,4],['data','science'],[25.32,34]]
Flatten_list = []

for i in list:
    if type(i) == list:
        Flatten_list.extend(i)
    else:
        Flatten_list.append(i)

print(Flatten_list)
