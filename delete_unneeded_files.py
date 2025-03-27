import os
from pathlib import Path

my_path = Path('/Users/****/Documents/Personal/python/Automate Boring stuff')

size_threshold = 1000

for folders, subfolders, filenames in os.walk(my_path):
    for filename in filenames:
        if os.path.exists(filename):
            file_size= os.path.getsize(filename)
            if file_size > size_threshold:
                print(f'Deleted {filename} with size: {file_size}')