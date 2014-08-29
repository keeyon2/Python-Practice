def Add2Nums (x, y):
	print 'Ran add 2 Nums'
	return x + y

def FunctionLabeling(a, b):
	foo(a, b)
	return

def RunFunctionOnInputs(function, input1, input2):
	function(input1, input2)
	return

foo = Add2Nums
RunFunctionOnInputs(foo, 1, 2)

x = 1

def SetNormal ():
	x = 2
	return x

def SetGlobal ():
	global x
	x = 2
	return x

print '''
print x
print SetNormal()
print x
'''
print x
print SetNormal()
print x

print '''
print x
print SetGlobal()
print x
'''

print x
print SetGlobal()
print x

