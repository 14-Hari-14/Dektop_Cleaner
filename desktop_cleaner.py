#program to create a script that will clean and organize files into folders
import os
import shutil
#logic for this code 
'''
if there is no directory then create one
put all the photos .pnj, ,jpg, .jpeg, in the photos folder
put all the documents .pdf, .txt, .docx in the docs folder
.mp4, .mov in the videos folder 
and all miscelaneous stuff in the other folder
'''

#function to create a folder if it doesnt exist
def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def organize_files(area_path):
    files = os.listdir(area_path)

    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Others": []  # Default folder for other file types
    }

    for file in files:
        file_path = os.path.join(area_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            destination_folder = None
            for folder_name, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder_name
                    break

            if destination_folder is None:
                destination_folder = "Others"

            destination_path = os.path.join(area_path, destination_folder)
            create_folder_if_not_exists(destination_path)
            shutil.move(file_path, os.path.join(destination_path, file))
    print("Succesfully managed")

if __name__ == "__main__":
    area = str(input("Enter the directory you want to manage: "))
    area_list = ["Desktop", "Documents", "Music", "Pictures", "Videos", "Downloads"]
    if area in area_list:
        area_path = os.path.join(os.path.expanduser("~"), area)
        organize_files(area_path)
    else:
        print("Incorrect directory mentioned")
