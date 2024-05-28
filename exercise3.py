#name ,ch=input("enter user name and character to count").split(",")
#print(f"{len(name)}  {(name.lower()).count(ch.lower())}")

#here if we eneter character prefix with space then output will be wrong
#use strips methods to remove spacev
name ,ch=input("enter user name and character to count").split(",")
print( f"{len(name)}  {name.strip().lower().count(ch.strip().lower())}")
