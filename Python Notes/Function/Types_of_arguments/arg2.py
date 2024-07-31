def multipy(*args):
    print("args>>", args)
    mul = 1

    for num in args:
        mul*= num
    print(f"multipy", mul)
    return mul

multipy(1,2,3,4,5)