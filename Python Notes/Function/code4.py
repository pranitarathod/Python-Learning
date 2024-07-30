def even_odd(input):
    even_list = []
    odd_list = []

    for item in input:
        if item%2 ==0:
            even_list.append(item)
        else:
            odd_list.append(item)
    print(f"EVEN_LIST == {even_list}")
    print(f"ODD_LIST == {odd_list}")

even_odd([34,89,65,45,34,12,78,111,74,34,90,122])
