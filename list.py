l=[]
#l[0]='grapes' error
#l[1]=67 error
l.append('grapes')
l.append(3)
print(l)

l.insert(1,'mango')
print(l)

l1=[1,2,3]
l2=['four','five','six',7]

l3=l1+l2
print(l3)

#concate l1 AND l2 and store answer into l1
print("concate using extend method")
l1.extend(l2)
print(l1)

print("using append  method it will create list inside list")
l1.append(l2)
print(l1)
