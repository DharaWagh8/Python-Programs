fruits=['orange','mango','kiwi','grapes']
print(fruits)
fruits.pop()
print(fruits)
#by default pop methhod will delete the last elemnt of the list
#to delete particular element we have to pass the position of the element
fruits.pop(0)
print(fruits)

#del method
print('delete elemEnt using delete method')
del fruits[0]
print(fruits)
#REMOVE METHOD
#used when we dont know the position of the elemnt to be deleted
fruits=['orange','mango','kiwi','grapes']
fruits.remove('grapes')
print(fruits)
#when we try to remove the lement which is not there 
#error 

fruits=['orange','apple','mango','kiwi','apple','grapes']
print(fruits)
fruits.remove('apple')
print(fruits)#it will remove only first apple second will remain as it is