#Chapter 10 notes


# Exercise 10.1


def simple_sum(arg):
	'''Sums a given list of 
	uniform element types.''' 
	result = sum(arg)
	return result 


def nested_sum(arg):
	'''Sums a list of ints and
	lists with a for loop + 
	recursion to determine if 
	there are deeper levels of 
	nesting. 
	'''
	total = 0
	for x in arg: 
		if isinstance(x,list):
			total += nested_sum(x)
		else: 
			total += x
	return total 


def pythonic_sum(arg): 
	'''Sums a list of ints and lists. Utilizes 
	very idiomatic syntax for python. Arguably 
	the same as nested_sum, but does not use 
	recursion and will throw an error if there 
	are >1 level of nesting in the array.''' 
	result = sum(sum(x) if isinstance(x,list) else x for x in arg)
	return result 


def compiler_sum(arg): 
	'''Sums a list of ints and lists,
	using the flatten function from the 
	compiler.ast module. Handles multiple 
	levels of nesting, but it's deprecated 
	in Python 3.0. Sad face.'''
	from compiler.ast import flatten
	result = sum(flatten(arg))
	return result 

def itertools_sum(arg): 
	'''Sums a list of lists, using the 
	itertools module to flatten the list. 
	Filters for none types, then sums it. 
	'''
	import itertools
	result = list(itertools.chain.from_iterable(arg))
	result = sum(filter(None, result))
	return result




t = [1,2,3]
n = [1,2,[72,73],6]
m = [1,2,[72,73,[72,73]],6]
o = [[1,2,3,4,5,6],[None,2],[],[7,8,9]]

print 'Simple sum: ' + str(simple_sum(t)) 
print 'Nested sum: ' + str(nested_sum(n))
print 'Pythonic sum: ' + str(pythonic_sum(n))
print 'Compiler sum: ' + str(compiler_sum(m))
print 'Itertools sum: ' + str(itertools_sum(o))



