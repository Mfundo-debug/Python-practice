import os 
import shutil

source = input("Enter the source folder name: ")
destination = input("Enter the destination folder name: ")

files = os.listdir(source)

moved_files = 0
not_moved_files = 0

for file in files:
    if file.startswith("AnimePahe_Tate_no_Yuusha_no_Nariagari"):
        shutil.move(os.path.join(source,file),os.path.join(destination,file))
        print("File moved successfully!")
        moved_files += 1
    else:
        not_moved_files += 1

print(f"Total files moved: {moved_files}")
print(f"Total files not moved: {not_moved_files}")