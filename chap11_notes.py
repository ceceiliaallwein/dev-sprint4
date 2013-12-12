# Chapter 11 notes


# Exercise 11.1




def keys_from_txt(filename): 
	with open(filename) as fin: 
		words = {}
		line = fin.readline()
		while line: 
			for line in fin:
				words[line.strip()] = True
		return words 

# DO NOT RUN THIS: infinite loop
# print keys_from_txt('words.txt')


# Histograms - strings 

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
print h.get('a',0)


def print_hist(h): 
	output = dict()
	for c in h:
		print c, h[c]

print_hist(h)
