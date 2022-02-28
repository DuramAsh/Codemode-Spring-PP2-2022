import os

print(os.getlogin())

print(os.getcwd()) # get current working directory

os.chdir("..")
print(os.getcwd())

# os.mkdir("Test_folder")

print(os.listdir(path="."))

os.chdir(r"C:\Users\adilz\Documents\Codemode-Spring-PP2-2022")
print(os.listdir(path="."))



