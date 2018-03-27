import os
from shutil import copyfile
import tkinter
from tkinter import filedialog

PREF_LOCATION = "uiprefs/"
SETTINGS_PATH = ".metadata/.plugins/org.eclipse.core.runtime/.settings/"

def move_files(parent_path):
    file_list = os.listdir(PREF_LOCATION)
    for file_name in file_list:
        print("copying " + file_name + "...")
        source = PREF_LOCATION + file_name
        destination = parent_path + SETTINGS_PATH + file_name
        copyfile(source, destination)
    print("file copy complete")
    
def retrieve_workspace():
    root = tkinter.Tk()
    root.withdraw()    
    file_path = filedialog.askdirectory() + "/"
    return file_path

if __name__ == "__main__":
    move_files(retrieve_workspace())