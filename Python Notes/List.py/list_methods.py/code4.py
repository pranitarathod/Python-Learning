list1 = [4,1,5,6,9,7,11,19,23,90,82]

odd_list = [data for data in list1 if data%2 !=0]
even_list =[data for data in list1 if data%2 == 0]

print(odd_list)
print(even_list)