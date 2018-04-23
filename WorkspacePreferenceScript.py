import os
from shutil import copyfile
import tkinter
from tkinter import filedialog
from tkinter import Listbox
from tkinter import Frame
from tkinter import Button


SCHEMES_LOCATION = "color schemes/"
SETTINGS_PATH = ".metadata/.plugins/org.eclipse.core.runtime/.settings/"

item_map = {}
list_box = None

def move_files(parent_path, scheme):
    print("sup")
    file_list = os.listdir(scheme)
    for file_name in file_list:
        print("copying " + file_name + "...")
        source = scheme + file_name
        destination = parent_path + SETTINGS_PATH + file_name
        copyfile(source, destination)
    print("file copy complete")
    
def retrieve_workspace():
    root = tkinter.Tk()
    root.withdraw()  
    file_path = filedialog.askdirectory() + "/"
    return file_path

def fetch_schemes():
    scheme_list = os.listdir(SCHEMES_LOCATION)
    return scheme_list
    
def create_list(frame):
    list_box = Listbox(frame, selectmode='single')
    i = 0
    for scheme in fetch_schemes():
        list_box.insert(i, scheme)
        item_map[i] = scheme
        i+=1
    return list_box 

def test():
    print("------")
    print("mark")
    print(retrieve_workspace())
    
    #list_input = list_box.curselection()
    #print(list_input)
    #if (len(list_input) == 0):
        #return
    #selected_scheme = item_map[list_input[0]]
    #print(selected_scheme)
    
def retrieve_scheme():
    root = tkinter.Tk()
    frame = Frame(root)
    button = Button(frame, text = "submit", command = test)
    button.grid(pady=10)   
    frame.pack()
    root.mainloop()
    return
    
    
    #global list_box
    #list_box = create_list(frame)
    #button = Button(frame, text = "submit", command = test)
    #button.grid(pady=10)
    #list_box.grid(padx = 20)
    #frame.pack()
    #root.mainloop()
    
    
    

if __name__ == "__main__":
    print("heyo")
    retrieve_scheme()
    #move_files(retrieve_workspace())
    #input("press enter to exit")