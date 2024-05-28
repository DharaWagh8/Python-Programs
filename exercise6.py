total=0
n=input("enetr number having more than one digit to sumup the digits: ")
l=len(n)
print(f"number of digits : {l} ")

for i in range(l):
    total+=int(n[i])

print(f"sum of digits of number {n} is {total}")