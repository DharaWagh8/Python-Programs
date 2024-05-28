

#list vs string
#string ara immutable
# list are mutable
s="hello"
t=s.title()
print(s)
print(t)
#we cant add characters to original string but we can add into list

l=['word1','word2','word3']
print(l)
l.pop()#it will change our original list
print(l)
l.append('word3')
print(l)
