s = input("Введите строку: ")
is_palindrome = True
n = len(s)
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")