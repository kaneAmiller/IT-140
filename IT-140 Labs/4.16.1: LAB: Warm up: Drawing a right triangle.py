triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range(triangle_height):  # assign the number of rows to triangle_height
    right_triangle = (triangle_char + ' ') * (i + 1)  # create the string and repeat it i+1 times (triangle_height)
    print(right_triangle)  # print the row
