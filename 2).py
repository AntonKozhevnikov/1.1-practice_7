l = str(input('Введите строку: '))
def is_palindrome(s):
    s = s.lower()
    s = s.replace(' ','')
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])
print(is_palindrome(l))

