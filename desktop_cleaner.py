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
#function to organize the files in specific folders
def organize_files(area_path):
    files = os.listdir(area_path)
    #dictionary to check various file extentions and organise them respectively
    folders = { 
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Others": []  # Default folder for other file types
    }
    #checkin for file in the list of all files copied from the directory
    for file in files:
        file_path = os.path.join(area_path, file) #creating an absolute file path of the file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower() #checking the extension of each file

            destination_folder = None #storing files according to the extensions
            for folder_name, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder_name
                    break

            if destination_folder is None:
                destination_folder = "Others"

            destination_path = os.path.join(area_path, destination_folder) #adding files to those newly or previously created folders
            create_folder_if_not_exists(destination_path)
            shutil.move(file_path, os.path.join(destination_path, file))
    print("Succesfully managed") #displaying the completion of the program

if __name__ == "__main__": #entry point of the program
    area = str(input("Enter the directory you want to manage: ")) #checking which directory to manage
    area_list = ["Desktop", "Documents", "Music", "Pictures", "Videos", "Downloads"] #list of valid direcotry names edit this to add personal direcotry names
    if area in area_list:
        area_path = os.path.join(os.path.expanduser("~"), area)
        organize_files(area_path)
    else:
        print("Incorrect directory mentioned") #stopping the program if incorrect file name is mentioned
