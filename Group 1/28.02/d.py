import os
# 1) Создать или открыть файл или папку
# 2) Перемещение между директориями
# 3) Удаление файлов и папок
# 4) Список доступных директорий

while True:
    command = input()

    if command == 'cd':
        kuda = input()
        if os.path.isdir(kuda) and os.path.exists(kuda):
            os.chdir(kuda)
            print("Done")
        else:
            print("Not a directory")
    
    elif command == 'dir':
        print(os.listdir(os.getcwd()), sep='\n')

    elif command == 'gdeya':
        print(f'The current directory is: [{os.getcwd()}]')

    elif command == 'del':
        chto = input()
        if os.path.exists(chto):
            os.remove(chto)
            print("done")
        else:
            print("there is no such file")

    elif command == 'create dir':
        imya = input()
        if os.path.exists(imya):
            print("Uzhe est'")
        else:
            os.mkdir(imya)
            print(f"Created {imya}")

    elif command == 'create file':
        imya = input()
        if os.path.exists(imya):
            print("Uzhe est'")
        else:
            f = open(imya, 'w')
            s = input("Che napisat'?\n")
            f.write(s)
            f.close()
            print(f"Created {imya}")
    elif command == 'exit':
        break