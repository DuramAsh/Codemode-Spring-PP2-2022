import re

emails = [
    'duramash.02@gmail.eDuCaT12iON',
    'duramash.02@gmail.com8239_048',
    'z_ashim@kbtu.kz',
    'shara32@tatarin.ru',
    'vovka25&it.mysyk',
    'qwerty@sdfgh'
]
# st = 'helloworld'
# pattern = '^hello$'
pattern = r'^(.+)@(\w+)\.([a-z]+)$'
for email in emails:
    if re.match(pattern, email):
        print(f'Email {email} is valid!')
    else:
        print(f'Email {email} is NOT valid!')

# pattern = r'(1299|1[3-8]\d{2}|19[0-1]\d|192[0-2])\s(0[1-9]|1[0-2])\s(0[1-9]|[1-2]\d|30|31)'
