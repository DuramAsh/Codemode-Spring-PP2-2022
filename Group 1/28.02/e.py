import os

s = os.getcwd()
ss = input("Old name:\n")

old_path = s + f"\{ss}"
print(old_path)

new_name = input("New name:\n")
new_name_path = (s + f"\{new_name}")
os.replace(old_path, new_name_path)