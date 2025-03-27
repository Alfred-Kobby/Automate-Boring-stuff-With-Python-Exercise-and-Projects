import os, shutil
from pathlib import Path

my_path = Path('/Users/aternor/Documents/Personal/python/Automate Boring stuff')

os.makedirs('my_new_folder', exist_ok=True)

patterns = ['*.pdf', '*.jpg']

for pattern in patterns:
    for filename in Path.glob(my_path, pattern):
        shutil.copy(filename, 'my_new_folder')

print("Done")