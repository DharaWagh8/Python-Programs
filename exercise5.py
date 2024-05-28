n=input("enter number having more than one digit")
#"1256" lenght=4  last index=3
#int(n[i])
total =0
i=0
while i<len(n):
    total +=int(n[i])
    i+=1
print(f"Total is :{total}") 
