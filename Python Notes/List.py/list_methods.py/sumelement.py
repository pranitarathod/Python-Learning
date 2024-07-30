def my_fun(item):
    sum_no = 0

    for i in item:
        sum_no += i
        return sum_no
    
print(my_fun([22,34,65,25]))

#or

list = [12,23,34,56,67,78,99]
add = sum(list)
print(f"sum of list: {add}")
