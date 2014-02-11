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
        self.regularExpressionString = None
        self.fileManager = FileManager()
        self.inputFile = None
        self.fileToProcess = StringVar()
        self.parent = parent
        Label(text="File to process", bg = 'grey' ).place(x=10, y = 80)
        self.toProcessEntry = Entry(textvariable=self.fileToProcess)
        self.toProcessEntry.place(x=100, y = 80)
        self.initUI()

    def initUI(self):
        # Here we can set the title of the tk window
        self.parent.title("RegEx Remover")
        #pack organises widgets into vertical and horizontal boxes. It is one of three geometry managers
        #expanded in both directions
        self.pack(fill=BOTH, expand=1)
        self.uploadFileButton = Button(text = "Upload file", command=self.upload_file_button_press)
        self.uploadFileButton.place(x=10, y=50)

    def upload_file_button_press(self):
        self.fileManager.openFile()
        # Given the complete path, this produces the string filename.extension
        path_to_input_file = self.fileManager.inputFile.name
        inputFileName = os.path.basename(path_to_input_file)
        self.fileToProcess.set(inputFileName)  
        # Once a file is upload - a button is placed to view it
        # Here is the windows configuration. For Ubuntu, change notepad to gedit
        viewInputFileButton = Button(text = "View input file", command=lambda:os.system('notepad ' + path_to_input_file) )
        viewInputFileButton.place(x=100, y = 50)
        reg_ex_entry_y_coordinate = 100
        Label(text="Reg Ex Entry", bg = 'grey' ).place(x=10, y = reg_ex_entry_y_coordinate)
        self.regExEntry = Entry().place(x = 100, y = reg_ex_entry_y_coordinate )
        processFileButton = Button(text = "Process file", command=self.process_file_button_press)
        processFileButton.place(x = 80, y = 120)

    def process_file_button_press(self):
        fileAsString = self.fileManager.inputFile.read()
        pattern = re.compile(self.regExEntry.get())
        outputFilePath = self.fileManager.openFile()
        outputFile = open(outputFilePath, 'w+')
        outputFile.write(pattern.sub(self.regExEntry.get(), fileAsString))
        outputFile.close()
        

def main():

        root = Tk()
        fileToProcess = None
        #window size
        root.geometry("250x150+300+300")
        app = RegExRemoverGUI(root) #this root is the parent variable
        root.mainloop()
        fileToProcess = None
        fileManager = FileManager()

if __name__ == '__main__':
    main()



