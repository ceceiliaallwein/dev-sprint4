#Chapter 10 notes


# Exercise 10.1


def simple_sum(arg):
	result = sum(arg)
	return result

t = [1,2,3]
print simple_sum(t)


def nested_list(arg):
	total = 0
	for x in arg: 
		result = simple_sum(arg)
		print result
	result = sum(result)
	return result

def nested_list2(arg): 
	total = 0 
	for num in arg: 
		total += simple_sum(arg)
	return total

n = [1,2,[72,73],6]
print nested_list(n)


