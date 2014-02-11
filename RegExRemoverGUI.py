__author__ = 'ian.polding'

from Tkinter import Tk, Frame, BOTH, Button, Entry, Label, StringVar
import tkFileDialog
from FileManager import FileManager
import tkMessageBox
import re
import os

class RegExRemoverGUI(Frame):

    processingButton = Button

    def __init__(self, parent):
        # we call the constructor of Frame - the inherited class
        Frame.__init__(self, parent, background='grey')
        #we store a reference to the parent widget - in this case it is Tk root window
        self.file_to_process = None
        self.regular_expression_string = None
        self.fileManager = FileManager()
        self.inputFile = None
        self.file_to_process = StringVar()
        self.parent = parent
        Label(text="File to process", bg = 'grey' ).place(x=10, y = 80)
        self.to_process_entry = Entry(textvariable=self.file_to_process)
        self.to_process_entry.place(x=100, y = 80)
        self.reg_ex_entry = Entry()
        self.initUI()

    def initUI(self):
        upload_file_x_coordinate = 10
        # Here we can set the title of the tk window
        self.parent.title("RegEx Remover")
        #pack organises widgets into vertical and horizontal boxes. It is one of three geometry managers
        #expanded in both directions
        self.pack(fill=BOTH, expand=1)
        self.upload_file_button = Button(text = "Upload file", command=self.press_upload_file_button)
        self.upload_file_button.place(x=upload_file_x_coordinate, y=50)

    def press_upload_file_button(self):
        self.fileManager.open_file()
        # Given the complete path, this produces the string filename.extension
        path_to_input_file = self.fileManager.input_file.name
        input_file_name = os.path.basename(path_to_input_file)
        self.file_to_process.set(input_file_name)  
        # Once a file is upload - a button is placed to view it
        # Here is the windows configuration. For Ubuntu, change notepad to gedit
        view_input_file_button = Button(text = "View input file", command=lambda:os.system('notepad ' + path_to_input_file) )

        view_input_file_button.place(x=100, y = 50)
        reg_ex_entry_y_coordinate = 100
        Label(text="Reg Ex Entry", bg = 'grey' ).place(x=10, y = reg_ex_entry_y_coordinate)
        # make the regular expression entry box visible by only placing it after a file is uploaded
        self.reg_ex_entry.place(x = 100, y = reg_ex_entry_y_coordinate)
        process_file_button = Button(text = "Process file", command=self.press_process_file_button)
        process_file_button.place(x = 10, y = 120)

    def press_process_file_button(self):
        fileAsString = self.fileManager.input_file.read()
        pattern = re.compile(self.reg_ex_entry.get())
        outputFilePath = self.fileManager.save_file()
        outputFile = open(outputFilePath, 'w+')
        outputFile.write(pattern.sub(self.regExEntry.get(), fileAsString))
        outputFile.close()
        view_output_file_button = Button(text = "View output file", command=lambda:os.system('notepad ' + path_to_input_file) )
        view_output_file_button.place(x=100, y = 120)
        

def main():

        root = Tk()
        file_to_process = None
        #window size
        root.geometry("250x150+300+300")
        app = RegExRemoverGUI(root) #this root is the parent variable
        root.mainloop()
        file_to_process = None
        fileManager = FileManager()

if __name__ == '__main__':
    main()
