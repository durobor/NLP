import sys

def sum(lower,upper):
    if lower == upper:
        return upper 
    else:
        return lower + sum(lower+1, upper) 

print sum(int(sys.argv[1]), int(sys.argv[2]))
