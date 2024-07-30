list1 = [10,20,30,40,50]
list2 = list1.copy()

print(id(list1))
print(id(list2))

print("list1 >>",list1)
print("list2 >>",list2)

list2.append("python")

print("list2 >>",list2)
print("list1 >>",list1)