def max_no(a,b):
    if a>b:
        return a
    return b

a1,b1=input("enter two numbers separted by commo").split(",")
print(f"from {a1}  and {b1} greater number is:")
print(max_no(int(a1),int(b1)))