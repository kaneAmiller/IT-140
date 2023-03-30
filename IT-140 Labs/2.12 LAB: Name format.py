full_name = input()
name_tokens = full_name.split(' ')
temp = '.'.join([name_tokens[i][0] for i in range(0, len(name_tokens) - 1)])
if temp == '':
    print(name_tokens[-1])
else:
    print(name_tokens[-1] + ', ' + temp + '.')
