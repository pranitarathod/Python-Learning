'''
Arbitary Keyword argument 

**kwargs

We don't know the number of default or keyword argument to be passed

datatype of kwargs is dictionary 
'''

def test(a,b ,c,**kwargs):
    print(f"A={a} B={b} C={c}")
    print(f"kwargs", kwargs)

test(a=10,b=23,c=56,d=22,e=87)
