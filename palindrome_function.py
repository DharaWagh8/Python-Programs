def is_palindrome(word):
    reversed_word=word[: :-1] #word[ : :-1]
    if word==reversed_word:
        return "it is palindrome"
    return "it is not palindrome"


#def is_palindrome(word):
#   return word ==word[: :-1]

s=input("enetr a string to check whether it is palindrome or not enter withoutspace at ending : ")
print(f"{s} : {is_palindrome(s)}")
print(is_palindrome("nayan"))
print(is_palindrome("dhaara"))
