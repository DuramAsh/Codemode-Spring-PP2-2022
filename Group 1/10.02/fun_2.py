def cap(s):
    s = "hello"
    print(s)
    
s = 'Leetcode'
cap(s)
print(s)

def fun():
    global s
    s = 'hello'
    print(s)
    
fun()
print(s)
print('-'*20)

def args(*words):
    print(words[0])
    print(words[1])

args("Adil", 'Ernat', 'Lera', 'Nazarbaev')

def kwargs(**mm):
    print(mm['f_name'])
    print(mm['s_name'])

kwargs(f_name = 'Kasym-Zhomart', s_name='Tokaev')

