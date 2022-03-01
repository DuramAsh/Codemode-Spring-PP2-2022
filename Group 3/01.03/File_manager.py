import os
# Используя ООП, реализуйте класс File_manager

# Основные фичи:
# 0) Показать текущее местоположение - os.getcwd()
# 1) Менять местоположение - os.chdir('dir_name')
# 2) Создавать папки - os.mkdir('dir_name')
# 3) Создавать файлы - open('file_name', 'w')
# 4) Получить список файлов и папок в текущей папке - os.listdir(path)
# elif command == 'dir'

# Допилите файл менеджер:
# 1) При команде dir выводите также колво папок и колво файлов (а также чтобы оно было как в cmd)
# 2 Каунтера, отдельно для isdir и для isfile
# 2) Сделать возврат в папку "C:\\"

# Добавить фичи для работы с файлами:
# 1) Переименовывание файлов - os.rename(old_name, new_name)
# 2) Добавить что-то в уже существующий файл (open(filename.txt, 'a'))
# 3) Переписать данные текущего файла в другой файл os.replace()

# my_file_manager = File_manager()

class File_manager():
    def __init__(self):
        pass
    
    def getCurrentPos(self):
        return os.getcwd()
    
    def changeDirectory(self, dir):
        try:
            os.chdir(dir)
            print("Success")
        except FileNotFoundError:
            print("Dir not found")
    
    def makeDirectory(self, name):
        try:
            os.mkdir(name)
            print("Success")
        except Exception:
            print("Error")

    def makeFile(self, name):
        try:
            open(name, "w").close()
            print("Success")
        except Exception:
            print("Error")
    
    def show(self):
        cntFile, cntDir = 0, 0 
        for file in os.listdir():
            if os.path.isdir(file):
                print(f"<DIR> {file}")
                cntDir += 1
            elif os.path.isfile(file):
                print(f"<FILE> {file}")
                cntFile += 1
        print(f"Files:{cntFile}\nDirs:{cntDir}")
        
    def toRoot(self):
        while os.getcwd() != 'C:\\':
            os.chdir('..')
    
    def rename(self, oldName, newName):
        try:
            os.rename(oldName, newName)
            print("Success")
        except Exception:
            print("Error")
    
    def add(self, name):
        newContent = input()
        with open(name, 'a') as wf:
            wf.write(newContent)

    def replace(self, oldName, newName):
        try:
            os.replace(oldName, newName)
            print("Success")
        except:
            print("Error")

mfm = File_manager()
while True:
    command = input()
    if command == "getpos":
        print(mfm.getCurrentPos())
    elif command == "changeDir":
        mfm.changeDirectory(input())
    elif command == "makeDir":
        mfm.makeDirectory(input())
    elif command == "makeFile":
        mfm.makeFile(input())
    elif command == "dir":
        mfm.show()
    elif command == "toRoot":
        mfm.toRoot()
    elif command == "rename":
        mfm.rename(input(),input())
    elif command == "add":
        mfm.add(input())
    elif command == "replace":
        mfm.replace(input(),input())
    elif command == 'exit':
        break
        



