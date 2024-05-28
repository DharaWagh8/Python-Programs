#find method
#replace method

string="she is very beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))

print(string.find("is"))
is_pos1=string.find("is")#is_pos1is integer variable to store first postion of 'is'
is_pos2=string.find("is",is_pos1+1)#is_pos2 is integer variable to store second postion of 'is' start index 
                                #for search is after first is which is stored in is_pos1
print(is_pos2)
print(string.find("she"))
print(string.find("she",3))
