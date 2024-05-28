def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c

print(greatest(1,3,6))

# function inside function

def new_greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c) #greater(greater(a,b),c)

print(new_greatest(1,3,5))