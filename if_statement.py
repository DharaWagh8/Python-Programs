
#else staemnet is optional but if it is ther its comes after if staemnet only
#else statement can't be there without if statement 
number1,number2=(input("enter number").split(","))
number1=int(number1)
number2=int(number2)
if number1>number2 :
    print("we are in if block")
    print("number1 is greter than number2")
else :
    print("we are in else block")
    print("number2 is greater than number1")