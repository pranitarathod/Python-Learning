def additon(*args):
    print(f"arbitary argument: {args}")
    print(type(args))
    
    total = 0
    for data in args:
        print(data)

additon(10,23,24)  