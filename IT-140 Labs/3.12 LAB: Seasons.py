input_month = input().lower()
input_day = int(input())

months = ('january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december')

if input_month not in months:
    print('Invalid')
else:
    if input_month == 'january':
        if not (0 < input_day <= 31):
            print('Invalid')
        else:
            print('Winter')
    elif input_month == 'february':
        if not (0 < input_day <= 28):
            print('Invalid')
        elif input_day <= 19:
            print('Winter')
        else:
            print('Spring')
    elif input_month == 'march':
        if not (0 < input_day <= 31):
            print('Invalid')
        elif input_day <= 19:
            print('Winter')
        else:
            print('Spring')
    elif input_month == 'april':
        if not (0 < input_day <= 30):
            print('Invalid')
        else:
            print('Spring')
    elif input_month == 'may':
        if not (0 < input_day <= 31):
            print('Invalid')
        else:
            print('Spring')
    elif input_month == 'june':
        if not (0 < input_day <= 30):
            print('Invalid')
        elif input_day <= 20:
            print('Spring')
        else:
            print('Summer')
    elif input_month == 'july':
        if not (0 < input_day <= 31):
            print('Invalid')
        else:
            print('Summer')
    elif input_month == 'august':
        if not (0 < input_day <= 31):
            print('Invalid')
        elif input_day <= 31:
            print('Summer')
        else:
            print('Invalid')
    elif input_month == 'september':
        if not (0 < input_day <= 30):
            print('Invalid')
        elif input_day <= 21:
            print('Summer')
        else:
            print('Autumn')
    elif input_month == 'october':
        if not (0 < input_day <= 31):
            print('Invalid')
        else:
            print('Autumn')
    elif input_month == 'november':
        if not (0 < input_day <= 30):
            print('Invalid')
        else:
            print('Autumn')
    elif input_month == 'december':
        if not (0 < input_day <= 31):
            print('Invalid')
        elif input_day <= 19:
            print('Winter')
        else:
            print('Spring')
