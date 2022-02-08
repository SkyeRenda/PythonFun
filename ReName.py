import os
from tkinter import Tk, filedialog, messagebox
from pathlib import Path


folders = []
done = False

def create_folder_list():
    i = 0
    x = 1
    open_main_folder = filedialog.askdirectory() # Returns opened path as str
    #Iterate through the chosen folder
    with os.scandir(open_main_folder) as folders:
        for folder in folders:
            #Iterate through the sub-folders
            with os.scandir(folder) as sub_folders:
                for file in sub_folders:
                    #Check if the file list is the list of images, if not restart the function
                   if (os.path.isfile(file) != True):
                        messagebox.showerror("Error", 'Please select a project folder with one layer of sub-folders.')
                        return False
                    #Rename the files
                   else: 
                        new_directory = folder.path + '/' + f"{x} ({i})"
                        os.rename(file, new_directory)
                        i+=1
                x += 1
                i = 0
    messagebox.showinfo("Success", 'The files have been renamed')  
    return True    

while (done == False):
    done = create_folder_list()
