import os
from File_manager import File_manager

mfm = File_manager()

while True:
    command = input()
    if command == 'cd':
        mfm.change_pos(input())
    elif command == 'dir':
        mfm.all_dir()
    elif command == 'makedir':
        pass
    