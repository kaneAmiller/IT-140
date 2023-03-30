name = print('What is your name?')
name = input()
age = print('How old are you?')
age = int(input())

from datetime import date

year = date.today().year
year_born = year - age

print('Hello {name}! You were born in {year}.'.format(name = name, year = year_born))
