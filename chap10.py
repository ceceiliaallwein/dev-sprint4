# Notes + answers to exercises in Ramp Up dev-sprint4 
# Ceceilia Allwein

# woo a change for git!


# Exercise 10.7 - anagrams

def is_list(string):
    x = list(string)
    return x

def sort_list(string):
    x = list(string)
    x.sort()
    return x

def is_anagram(string1,string2):
    '''Determines if two words can
    be arranged to spell each other.
    '''
    x = sort_list(string1)
    y = sort_list(string2)
    if len(x) != len(y):
            return False
    else: 
        for i in range(len(x)): 
            if x[i] == y[i]:
                return True
            else: 
                return False

print ''
print 'Exercise 10.7 - is_anagram'
print is_anagram('moon','nomo')


# Exercise 10.13 - interlocking words 

print ''
print 'Exercise 10.13 - interlock'

def switch(x,y):
    x,y = y,x
    return x,y


def match_txt(word,filename):
    '''Determines if a given word
    appears in a text file.
    '''
    with open(filename) as fin:
        line = fin.readline()
        output = []
        while line:
            plain = line.strip() 
            if word == plain: 
                output.append(word)
                return output
            line = fin.readline()
        else: 
            return output
        return  output

output = []

def interlock1(word1,word2,filename): 
    '''Takes alternating letters of
    two given words and combines them
    into one, interlocking string.

    Returns False if input strings are 
    not of similar length, i.e. there 
    are "leftover" letters from one 
    word that do not interlock. 

    word1 = string
    word2 = string  
    '''
    x = is_list(word1)
    y = is_list(word2)
    difference = len(x) - len(y)
    if difference <= 1 and difference >= -1:
        # If I give None a different name it's ID'd as a global variable.
        # Why is it not just a placeholder? 
        result = [None]*(len(x)+len(y))
        result[::2] = x
        print result
        result[1::2] = y
        result = "".join(result)
        result = match_txt(result,filename)
        # why is this pythonic? 
        if not result: 
            return False
        # is this dead code? 
        else:    
            result = '\n'.join(result)
            return result
    else: 
        return "Please try again with words of equal length."

print 'Interlock 1: ' + str(interlock1('warmed','cold','words.txt'))


def interlock2(filename):
    '''Scans a text file for words of 
    equal length, then determines if they 
    interlock to form a new word.'''
    with open(filename) as fin:
        x = fin.readline()
        y = fin.readline()
        while True: 
            if len(x) == len(y):
                result = interlock1(x,y,filename)
                output.append(result)    
            x = y
            y = fin.readline()
            print x 
            print y
        print output
        return output

'''
PROBLEMS 
The interlock loop ends when it finds two words of equal length.
(Solution: modify to add each result of interlock to output = [])

PUNCH LIST 
> Use bisection search to reduce processing time of match_txt
> Generalize to accommodate any number of words of any length
(Solution: modify the step, i.e. third parameter in the slice.)
> Generalize to accommodate words of any length
(Solution: I don't think the slice approach will work for words where 
the difference in len is great than n+/-1 b/c you end up with None 
types in result arrays in interlock. You could replace them--or delete--
but ugh. There has to be a better way.)
> Modify so that it tries interlocking words in range i in 
every possible combination. 
'''


#print interlock2('words.txt')

