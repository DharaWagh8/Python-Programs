age=int(input("enter the age "))
if age==0 or age<0 :
    print("please enter valid age:")
elif 0<age<=3:
    print("ticket prices :free ")
elif 3<age<=10:
    print("ticket price:150")
elif 10<age<=60:
    print("ticket price :200")
else:
    print("ticket price :250")
