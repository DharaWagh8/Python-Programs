x=5
def fun1():
    x=4
    return x

print(x)
print(fun1())
print(x)

y=5
def fun2():
    global y
    y=4
    return y

print(y)
print(fun2())
print(y)