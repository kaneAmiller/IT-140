user_text = input()

invalid_char = ' ,.'
char_count = 0
for character in user_text:
    if character not in invalid_char:
        char_count += 1
    else:
        continue
print(char_count)
