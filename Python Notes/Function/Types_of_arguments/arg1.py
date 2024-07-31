def addition(n1,n2,*args,x = 20, y = 100 ):   #### Order 1 positional and arbitary and default argument 
    print(f"n1=={n1} and n2={n2}")
    print(f"arbitary Argument ={args}")
    print(f"X={x} and Y = {y}")
    print(type(args))
    
    total = 0
    for data in args:
        total = total + data
    
    return total

no1 = 10
no2 = 20
no3 = 30 
no4 = 50
no5 = 60

add = addition([12,30,40],[10,20,30],no1,no2,no3,no4,no5)
print(add)
avg = add/10
print(avg)