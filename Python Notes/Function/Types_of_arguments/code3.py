def test(a,b,c,**kw):
    print(f"A={a} B={b} C ={c}")
    print(f"kwargs={kw}")
    
test(c=30,a=10,b=20,d=50,e=50,f='python')