def sqrlist(start,end):
    list1 = [num**2 for num in range(start,start+5)]
    list2 = [num**2 for num in range(end-4,end+1)]
    print(list2)
    # list3 = list1 + list21
    # print(list3)

start_num = int(input("ENTER START NO:"))
end_num = int(input("ENTER end NO:"))


sqrlist(start_num,end_num)