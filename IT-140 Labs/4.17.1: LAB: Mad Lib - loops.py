user_input = input()

while user_input != 'quit':  # start loop
    if 'quit' in user_input:
        break  # break if user entered 'quit'
    madlib_list = user_input.split()  # split the number and noun to be formatted
    print("Eating {} {} a day keeps the doctor away.".format(int(madlib_list[1]), madlib_list[0]))
    user_input = input()  # get the next input
