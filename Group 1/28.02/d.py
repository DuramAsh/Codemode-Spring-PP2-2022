import os
# 1) Создать или открыть файл или папку
# 2) Перемещение между директориями
# 3) Удаление файлов и папок
# 4) Список доступных директорий

while True:
    command = input()

    if command == 'cd':
        kuda = input()
        if os.path.isdir(kuda):
            os.chdir(kuda)
    
    elif command == 'dir':
        print(os.listdir(os.getcwd()), sep='\n')

    elif command == 'gdeya':
        print(f'The current directory is: [{os.getcwd()}]')

    elif command == 'exit':
        break