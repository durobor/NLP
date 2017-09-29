import sys

def f(n):
    r=1
    if 0==n:
        return r
    else:
        for i in range (1,n+1):
            r*=i
        return r

user_input = input("Enter an integer: ")
print'f(',user_input,') =',f(user_input)
