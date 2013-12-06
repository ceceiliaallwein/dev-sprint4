# Notes + answers to exercises in Ramp Up dev-sprint4 
# Ceceilia Allwein

# woo a change for git!


# Exercise 10.7 - anagrams

#def is_list(string1):

# def sort_str(string):

def sort_list(string):
    x = list(string)
    x.sort()
    return x

def is_anagram(string1,string2):
    '''Determines if two words can
    be arranged to spell each other.
    > Convert strings into lists 
    > Sort both lists into alpha order 
    > Alias string 2 as string1
    > string2 is string1
    > return boolean
    '''
    x = sort_list(string1)
    y = sort_list(string2)
    if y is x: 
        return True
    else: 
        return False

print is_anagram('sit','tis')


# Exercise 10.13 - interlocking words 