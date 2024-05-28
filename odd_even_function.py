def odd_even(a):
    if a%2 ==0:
        return "even"
    else:
        return "odd"
        
#   if a%2 ==0:
#      return "even"
#   return "odd"

print(odd_even(9))
print(odd_even(2))


def is_even(n):
    if n%2==0:
        return True
    return False

#same as above in different way
#def is_even(n):
#     return n%2==0 #true

print(is_even(3))


def sing():
    return "happy moments"
print(sing())