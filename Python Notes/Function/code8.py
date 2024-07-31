def even_odd_list(n):
    even_list = []
    odd_list = []

    for i in range(n):
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print("even_list:", even_list)
    print("odd_list:", odd_list)

even_odd_list(20)

