# Chapter 11 notes

def histogram(s): 
	d = dict()
	for c in s: 
		if c not in d: 
			d[c] = 1
		else: 
			d[c] += 1
	return d 

print histogram('ceceilia')

h = histogram('ceceilia')
print h

#print h.get('a',0)


def print_hist(h): 
	output = dict()
	for c in h:
		print c, h[c]

print_hist(h)
