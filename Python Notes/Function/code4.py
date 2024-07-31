
def even_odd(input):
    
    for i in range(n):
        item = int(input(f"enter the {i}value"))
        if item%2 ==0:
            even_list.append(item)
        else:
            odd_list.append(item)
    print(f"EVEN_LIST == {even_list}")
    print(f"ODD_LIST == {odd_list}")

n = int(input("Enter number of items:"))
even_list = []
odd_list = []
even_odd(input)
         
