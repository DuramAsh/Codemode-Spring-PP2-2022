import os
print(os.getcwd())
#Exception
try:
    os.chdir("test")
except Exception as e:
    print(e)
print("Success")