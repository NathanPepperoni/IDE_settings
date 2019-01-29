import os
from shutil import copyfile
import tkinter
from tkinter import filedialog

RUNTIME_PREF_LOCATION = "uiprefs/"
RUNTIME_SETTINGS_PATH = ".metadata/.plugins/org.eclipse.core.runtime/.settings/"
WORKBENCH_PREF_LOCATION = "workbenchprefs/"
WORKBENCH_SETTINGS_PATH = ".metadata/.plugins/org.eclipse.e4.workbench/"

def move_runtime_files(parent_path):
    file_list = os.listdir(RUNTIME_PREF_LOCATION)
    for file_name in file_list:
        print("copying " + file_name + "...")
        source = RUNTIME_PREF_LOCATION + file_name
        destination = parent_path + RUNTIME_SETTINGS_PATH + file_name
        copyfile(source, destination)
    
def move_workbench_files(parent_path):
    file_list = os.listdir(WORKBENCH_PREF_LOCATION)
    for file_name in file_list:
        print("copying " + file_name + "...")
        source = WORKBENCH_PREF_LOCATION + file_name
        destination = parent_path + WORKBENCH_SETTINGS_PATH + file_name
        copyfile(source, destination)  
    
def retrieve_workspace():
    root = tkinter.Tk()
    root.withdraw()    
    file_path = filedialog.askdirectory() + "/"
    return file_path

if __name__ == "__main__":
    workspace = retrieve_workspace()
    move_runtime_files(workspace)
    move_workbench_files(workspace)
    print("file copy complete")  
    #input("press enter to exit")