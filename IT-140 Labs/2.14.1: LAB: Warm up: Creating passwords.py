# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
color = input()
noun = input()
num = input()
print('You entered:', color + ' ' + noun + ' ' + num)

# FIXME (2): Output two password options
password1 = color + '_' + noun
password2 = num + color + num

print('\nFirst password:', password1)
print('Second password:', password2)

# FIXME (3): Output the length of the two password options
print('\nNumber of characters in',password1 + ':', len(password1))
print('Number of characters in', password2 + ':',len(password2))