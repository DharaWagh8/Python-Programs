#center method
name="Dhara"
#**Dhara** 9=5(length of string)+4(star length)
print(name.center(9,"*"))
#*Dhara* 9=5(length of string)+2(star length)
print(name.center(7,"*"))

print(name.center(6,"*"))

#problem statement :take user name as input add 4 star on both the side of name
name=input("enetr your name:")
print(name.center(len(name)+8,"*"))