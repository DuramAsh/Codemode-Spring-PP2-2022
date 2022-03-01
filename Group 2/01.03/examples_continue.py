import os

print(os.getcwd())
dirs = os.listdir(os.getcwd())
for i in dirs:
    if os.path.isdir(i):
        print(f'<DIR> {i}')
    elif os.path.isfile(i):
        print(f'<FILE> {i}')

path = input()
if os.path.isdir(path):
    os.chdir(path)
    print(os.getcwd())
else:
    print('Not a directory!')

# try:
#     os.chdir(path)
#     print(os.getcwd())
# except Exception as e:
#     print(str(e))