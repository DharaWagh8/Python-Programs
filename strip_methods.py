name="          Dhara           "
dots="..................."
print(name + dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
#strip methods can't remove space comes on between words
name="          Dhara         Wagh           "
dots="..................."
print(name + dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
#we can acheive it using replace method
print(name.replace(" ","")+dots)