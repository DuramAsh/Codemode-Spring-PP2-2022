import os
# Используя ООП, реализуйте класс File_manager

# Основные фичи:
# 0) Показать текущее местоположение - os.getcwd()
# 1) Менять местоположение - os.chdir('dir_name')
# 2) Создавать папки - os.mkdir('dir_name')
# 3) Создавать файлы - open('file_name', 'w')
# 4) Получить список файлов и папок в текущей папке - os.listdir(path)

# Допилите файл менеджер:
# 1) При команде dir выводите также колво папок и колво файлов (а также чтобы оно было как в cmd)
# 2 Каунтера, отдельно для isdir и для isfile
# 2) Сделать возврат в папку "C:\\"

# Добавить фичи для работы с файлами:
# 1) Переименовывание файлов - os.rename(old_name, new_name)
# 2) Добавить что-то в уже существующий файл (open(filename.txt, 'a'))
# 3) Переписать данные текущего файла в другой файл os.replace()

# my_file_manager = File_manager()


class File_manager:
    def __init__(self):
        pass

    def show_pos(self):
        print(os.getcwd())

    def change_pos(self, path):
        os.chdir(path)
        print('Completed Succesfully')
        self.showPosition()

    def create_dir(self, dir):
        try:
            os.mkdir(dir)
            print("Success")
        except Exception as e:
            print(str(e))

    def create_file(self, filename):
        try:
            open(filename, 'w').close()
            print('Success')
        except Exception as e:
            print(str(e))

    def all_dir(self, path):
        print(os.listdir(path))
        cnt_d, cnt_f = 0, 0
        for i in os.listdir(path):
            if os.path.isfile(i):
                cnt_f += 1
            elif os.path.isdir(i):
                cnt_d += 1
        print(f'Amount of files: {cnt_f}\nAmount of dirs: {cnt_d}')

    def default(self):
        self.change_pos('C:\\')

    def rename(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print("Success")
        except Exception as e:
            print(str(e))

    def add(self, filename, what):
        with open(filename, 'a') as f:
            f.write(what)

    def replace(self, old_name, new_name):
        old = str(os.getcwd() + '\\' +old_name)
        new = str(os.getcwd() + '\\' + new_name)
        os.replace(old, new)
        print('Success')