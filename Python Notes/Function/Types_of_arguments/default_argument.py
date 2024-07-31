'''
default argument/keyword argument (kwargs)
default argument will always follow positional argument.
key=value / this way rhe order of the arguments does not matter.
'''

def my_fun(a,b): # a and b are parameters
    print(f"a={a} and b ={b}")
    
    return a+b

print(my_fun(b = 30, a = 10))