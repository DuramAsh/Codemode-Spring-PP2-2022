def my_fun():
    return []

def my_fun2(a=5):
    print(a)
    if a == 10:
        return
    my_fun2(a + 1)
    
my_fun2(3)