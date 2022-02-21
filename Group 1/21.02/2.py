import re

emails = [
    'duramash.02@gmail.com',
    'duramash.02@gmail.com8239048',
    'z_ashim@kbtu.kz',
    'shara32@tatarin.ru',
    'vovka25&it.mysyk',
    'qwerty@sdfgh'
]
pattern = r'^.+@[a-z]+\.[a-z]+$'

for i in emails:
    if re.match(pattern, i):
        print(f'Email {i} is valid!')
    else:
        print(f'Email {i} is NOT vald!')

# * - [0; \infty)
# + - [1; \infty)
# ? - [0; 1]