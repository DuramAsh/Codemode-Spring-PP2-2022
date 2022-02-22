import re

emails = [
    'duramash.02@gmail.com', #Valid
    'duramash.02@gmail.com8239_048', #Not V
    'z_ashim@kbtu.kz', #Valid
    'shara32@tatarin.ru', #Valid
    'vovka25&it.mysyk', #Not Valid
    'qwerty@sdfgh' #Not valid
]

pattern = r'.+@[a-z]+\.[a-z]+$'

for email in emails:
    if re.match(pattern, email):
        print(f'Email {email} is valid')
    else:
        print(f'Email {email} is not valid')