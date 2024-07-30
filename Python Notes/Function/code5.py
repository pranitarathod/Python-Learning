
def even_odd(input_list):

    '''
    This function is separting even and odd list 
    items from given input list 
    '''

    even_list = [item for item in input_list if item%2==0]
    odd_list = [item for item in input_list if item%2!=0]

    print(f"even_list == {even_list}")
    print(f"odd_list == {odd_list}")

even_odd([12,23,45,32,11,45,36,77,65,33,79,88,90,55,57,89])