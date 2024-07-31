#default parameter

def addition(x=0,y=0,z = 0): ### x,y,x are parameters
    print(f"X ={x}, Y = {y}, Z= {z}")
    add = x+y+z
    
    return add

# Calling the function
no1 = int(input())
no2 = int(input())
print(addition(no1,30)) ### positional arguments