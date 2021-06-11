def f(my_list=[]):
	my_list.append('###')
	return my_list

def f0():
	return f([])

def i():
	return 1

l1 = ['foo', 'bar', 'baz']
print(f(l1))

l2 = ['foo', 'bar', 'baz']
print(f(l2))

print(f0())
print(f0())
print(f0())

print(i())
