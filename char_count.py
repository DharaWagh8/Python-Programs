s=input("enter string")
i=0
#dhara wagh
#s.count("d")     s.count(s[0])=1
#s.count("h")     s.count(s[0])=2
#s.count("a")     s.count(s[0])=3
#s.count("r")     s.count(s[0])=1
#s.count(" ")     s.count(s[0])=1
#s.count("w")     s.count(s[0])=1
#s.count("g")     s.count(s[0])=1
temp_var=""
while i<len(s):
    if s[i] not in temp_var:
        temp_var=temp_var+s[i]
        print(f"{s[i]}: {s.count(s[i])}")
    i+=1
