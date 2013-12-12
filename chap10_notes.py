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
	'''Sums a list of ints and lists. Arguably 
	the same as nested_sum, but does not use 
	recursion and will throw an error if there 
	are >1 level of nesting in the array.''' 
	result = sum(sum(x) if isinstance(x,list) else x for x in arg)
	return result 


def module_sum(arg): 
	'''Sums a list of ints and lists,
	using the flatten module from compiler. 
	Handles multiple levels of nesting.'''
	from compiler.ast import flatten
	result = sum(flatten(arg))
	return result 


t = [1,2,3]
n = [1,2,[72,73],6]
m = [1,2,[72,73,[72,73]],6]

print 'Simple sum: ' + str(simple_sum(t)) 
print 'Nested sum: ' + str(nested_sum(n))
print 'Pythonic sum: ' + str(pythonic_sum(n))
print 'Module sum: ' + str(module_sum(m))



