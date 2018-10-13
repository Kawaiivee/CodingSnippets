functions = {}

def foo():
    print('foo')
	
def fiz():
	print('fiz')

def baz():
    print('baz')

def bar():
    print('bar')

functions['b2']=bar
functions['a']=foo
functions['a1']=fiz
functions['b1']=baz

for fns in functions:
    functions[fns]()
