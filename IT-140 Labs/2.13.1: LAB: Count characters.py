input = input()
temp = input.split(' ')
char = temp[0]
temp = ' '.join(temp)
char_num = (temp.count(char)) - 1

print(char_num)
