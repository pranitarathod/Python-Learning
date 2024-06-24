#variables which are declared inside the function.
#we cannot access from outside the function.

var = "Global variable"

def my_func():
    var1 = "Local variable"
    print(" variable is " , var )
    print(" variable is " , var1)

my_func()