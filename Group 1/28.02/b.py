import os

os.chdir(r"C:\Users\adilz\Documents\Codemode-Spring-PP2-2022\Group 1\Test_folder")

# for i in range(10):
#     f = open(f'{i+1}.txt', 'w')
#     f.close()

for i in range(5):
    os.mkdir(f"{i+1}")
    os.chdir(os.path.join(os.getcwd(), f"{i+1}"))
