"""
 positional Arguments ==== number of positional arguments = number of parameter

 positional argument means that the argument must be provided in a correct position in a function call.

 """

def my_fun(a,b):
    print(f"a={a} and b={b}")
    add = a+b
    return add

print(my_fun(2,5))
 