import os
import shutil

path=input("enter folder path:"). strip()

for file in os.listdir(path):
    old_file_path = os.path.join(path, file)
    if not os.path.isfile(old_file_path):
        continue
    name, exe = os.path.splitext(file)
    ext = exe[1:]. lower()

    if not ext:
        continue
    folder_path = os.path.join(path, ext.upper() + "_Files")
    os.makedirs(folder_path, exist_ok=True)

    
    new_file_path = os.path.join(folder_path, file)
    shutil.move(old_file_path, new_file_path)


print("done organizing your files✨")




