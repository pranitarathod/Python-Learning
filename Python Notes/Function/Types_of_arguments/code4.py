def test(*args,**kw):
#     print(f"A={a} B={b} C ={c}")
    print(f"args ={args}")
    print(f"kwargs={kw}")
    total = sum(kw.values())
    per = total / len(kw.values()) * 100
    print(total)
    print(per)
    
test(10,20,30,a=10)