'''
*args--- >>> 

when we don't know number of arguments to pass

data types of these args varaible is always tuple.

if you dont know how many arguments that will be passed into your function , add * before the parameter name in the function definition.
'''

def addition(*args):
    print(f"*args={args}")
    print(type(args))

addition(10)