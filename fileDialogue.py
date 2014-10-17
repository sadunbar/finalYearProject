from Tkinter import *
from AddFile import addFile, delFile

root = Tk()
root.title("File Selection")
root.geometry('300x300+100+200')

def close_window (): 
    root.destroy()

addFileButton = Button(root, text = "Add File", command = addFile)
addFileButton.pack(side = RIGHT, padx = 5, pady = 5)

closeButton = Button(root, text="Close", command = close_window)
closeButton.pack(side = LEFT, padx = 5, pady = 5)

delFileButton = Button(root, text="Remove File", command = delFile)
delFileButton.pack(side = RIGHT, padx = 5, pady = 5)

root.mainloop()
