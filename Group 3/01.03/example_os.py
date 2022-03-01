import os
print(os.getcwd()) # Возвращает текущую директорию
# cd - chdir() - change directory
os.chdir("..")
os.chdir("..")
#print(os.getcwd())
#os.mkdir("Test dir")
#os.rename("Test dir", "test dir 2")
#os.rmdir("Test dir")
#open("Test file", "w").close()
#for file in os.listdir():
#    print(f"<DIR> {file}")
print(os.path.isfile("1.py"))
print(os.path.isdir("Group 3"))
if os.path.isdir("1.py"):
    os.chdir("1.py")
print(os.getcwd())