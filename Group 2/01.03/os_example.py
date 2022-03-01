import os

print('-' * 30)
print(os.getcwd()) # get current working directory
print(os.listdir('.'))
os.chdir('..')
print(os.listdir(os.getcwd()))
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('Group 2')
print(os.getcwd())
os.chdir('Test_folder')
os.chdir('..')
os.mkdir('Test_folder')
open('test_file.txt', 'w').close()
os.remove('test_file.txt')
os.rmdir('Test_folder')
