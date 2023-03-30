user_int = int(input('Enter integer (32 - 126):\n'))
user_flo = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_str = input('Enter string:\n')

print(user_int, user_flo, user_char, user_str)
print(user_str, user_char, user_flo, user_int)
print(user_int, 'converted to a character is', chr(user_int))
