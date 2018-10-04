functions = {}

def foo():
    print('foo')
    
def baz():
    print('baz')
    
functions['a']=foo
functions['b']=baz

for fns in functions:
    functions[fns]()
