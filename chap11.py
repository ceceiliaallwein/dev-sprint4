# Notes + answers to exercises in Ramp Up dev-sprint4 
# Name: Ceceilia Allwein


# Exercise 11.9 - has duplicates

def mk_d(filename): 
    with open(filename) as fin:
        output = dict()
        line = fin.readline()
        while line: 
            for line in fin:
                output[line] = 'var'
        return output

print mk_d('words.txt')

def has_dupes1(filename): 
    ''' Returns true if a value appears 
    more than once in a list.
    '''
    output = dict(mk_d(filename))
    for x in output:
        if x in output:
            return True
        output[x] = True
    return False

print has_dupes1('words.txt')


def has_dupes2(arg):  
    return len(set(arg)) < len(arg)


print has_dupes2('words.txt')


'''
if __name__ == '__main__':
    arg = [1, 2, 3]
    print has_dupes(arg)
    arg.append(1)
    print has_duplicates(arg)

    arg = [1, 2, 3]
    print has_duplicates2(arg)
    arg.append(1)
    print has_duplicates2(arg)
'''


# Exercise 11.10 - find rotate pairs 


