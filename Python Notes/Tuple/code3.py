#Tuple is faster than list 
#Tuple consume less memory space to store data

import sys
list = [11,12,13,14,23,33,44,35,76,65]
print(sys.getsizeof(list))

tuple = (12,14,23,15,67,34,75,78,67,44,88)
print(sys.getsizeof(tuple))