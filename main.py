def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

input_word = input("Введите строку: ")
is_pal = is_palindrome(input_word)
print(is_pal)