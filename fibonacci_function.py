def fibonacci_series(a):
    first=0
    second=1

    if a==1:
        print (first)
    elif a==2:
        print (first,second) 
    elif a>2:
        print (first,second,end=" ")
        for i in range(a-2):
            c=first+second
            first=second
            second=c
            print(c, end=" ")

# for i in range (1,11):
#   print(i,end=" , ") 
#





number =int(input("enetr to print a fibonacci series :"))
fibonacci_series(number)
