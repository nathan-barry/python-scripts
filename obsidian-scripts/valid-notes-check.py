import os
import re

path = r'/home/anon/Notes/Zettelkasten'
dir_list = os.listdir(path)

for dir in dir_list:
    with open(path+'/'+dir, 'r') as rf:
        lines = rf.readlines()

        if (lines[0] != '---\n' or
            lines[1][:8] != 'title: "' or
            lines[2][:7] != 'date: "' or
            lines[3][:6] != 'tags: ' or
            lines[4][:9] != 'aliases: ' or
            lines[5] != '---\n' or
            lines[6] != '\n' or
            lines[7] != '\n'):
            print(f"VALID FORMAT: {dir}")
            print(f"    Line 0: {lines[0]}", end='')
            print(f"    Line 1: {lines[1][:8]}\n", end='')
            print(f"    Line 2: {lines[2][:7]}\n", end='')
            print(f"    Line 3: {lines[3][:6]}\n", end='')
            print(f"    Line 4: {lines[4][:9]}\n", end='')
            print(f"    Line 5: {lines[5]}", end='')
            print(f"    Line 6: {lines[6]}", end='')
            print(f"    Line 7: {lines[7]}", end='')
            print()
