#enclosed scope(inner_fun can access outer_fun)
def outer_fun():
    msg="hello"
    msg2="idiot"
    print(msg)
    def inner_fun():
        print(msg+msg2)
    inner_fun()
outer_fun()
#outer_fun() cannnot directly acccess inner_fun()
#it has to intialize the var first in outer_function and make as non_local using keyword non_local
def add_fun():
    a=199
    b=200
    c=a+b
    res=""
    def inner_fun2():
        nonlocal res    # keyword "non-local"
        print(c)
        res="hello bro"
    inner_fun2()
    print(res)
add_fun()        
  