def square_list(start, end):

    list1 = [num**2 for num in range(start, (start+5))]
    list2 = [num**2 for num in range(end, (end+1))]

    list3 = list1 + list2

    print(list3)
    return 'list is done'

var = square_list(1,20)
print(var)