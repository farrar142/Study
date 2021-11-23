def test(a,b,test1):
    result = a+b
    test1(result)
    
test(1,2, lambda x: x+5)
print("how to use callback?")