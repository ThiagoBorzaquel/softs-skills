import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '{}[]()*;/,._-'

all = lower + upper + number + symbols

lenght = 16
password = ''.join(random.sample(all, lenght))

print(f'Sua senha é {password}')
