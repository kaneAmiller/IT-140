word = input()
password = ''

char_replace = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}  # assigns characters to be replaced

for char in word:  # assigns char as key and starts loop
    if char in char_replace:  # replaces invalid characters
        password += char_replace[char]
    else:  # if the character is valid, add it to the password
        password += char
password += 'q*s'  # adds q*s to the end of the password
print(password)
