import os

# 0) Показать текущее местоположение
# 1) Менять местоположение
# 2) Создавать папки
# 3) Создавать файлы
# 4) Получить список файлов и папок в текущей папке

print('-' * 30)
print(os.getcwd()) # get current working directory
print(os.listdir('.'))
os.chdir('..')
print(os.listdir(os.getcwd()))
# os.chdir('..')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# os.chdir('Group 2')
# print(os.getcwd())
# os.chdir('Test_folder')
# os.chdir('..')
# os.mkdir('Test_folder')
# open('test_file.txt', 'w').close()
# os.remove('test_file.txt')
# os.rmdir('Test_folder')
