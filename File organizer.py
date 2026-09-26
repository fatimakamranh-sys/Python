import os
import shutil

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
}

path=input("enter folder path:"). strip()

for file in os.listdir(path):
    old_file_path = os.path.join(path, file)
    if not os.path.isfile(old_file_path):
        continue
    name, exe = os.path.splitext(file)
    ext = exe[1:]. lower()

    if not ext:
        continue
    folder_name = "misc_files"
    for category, extensions in categories.items():
        if"." + ext in extensions:
            folder_name = category + "_files"
            break

    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    
    new_file_path = os.path.join(folder_path, file)
    shutil.move(old_file_path, new_file_path)


print("done organizing your files✨")




