fruits=['apple','orange','banana','grapes','kiwi']
numbers=[1,56,3,2,5,6,90]
print(fruits.count('orange'))

#copy method

cp_fruits=fruits.copy()
print(cp_fruits)

print(f"numbers before sort() method{numbers}")
#print(f"numbers after sort() method {numbers.sort()}")
#its not printing the sorted output :numbers after sort() method None
#numbers.sort()#it will sort original list
print(numbers)

#sorthed function
#if we want to print the sorted numbers 
print(sorted(numbers))
print(numbers)

numbers.clear()
print(numbers)