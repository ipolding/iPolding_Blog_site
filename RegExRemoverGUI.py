__author__ = 'ian.polding'

from Tkinter import Tk, Frame, BOTH, Button, Entry, Label
import tkFileDialog
import FileManager
import tkMessageBox
import re
import os

class RegExRemover(Frame):

    processingButton = Button

    def __init__(self, parent):
        # we call the constructor of Frame - the inherited class
        Frame.__init__(self, parent, background="white")
        #we store a reference to the parent widget - in this case it is Tk root window
        self.regularExpressionString = None
        self.fileManager = FileManager()
        self.inputFile
        self.currentFile
        self.initUI()






    def initUI(self):
        # Here we can set the title of the tk window
        self.parent.title("RegEx Remover")
        #pack organises widgets into vertical and horizontal boxes. It is one of three geometry managers
        #expanded in both directions
        self.pack(fill=BOTH, expand=1)
        self.uploadFileButton = Button(text = "Upload file", command=self.fileManager.openFile())
        self.processingButton.place(x=50, y=50)
        self.viewCurrentFileButton = Button(text = "View file in text editor", command=self.viewFile() )


    def viewFile(self):
        if self.currentFile:
            os.system('gedit ' + self.currentFile)
        else:
            tkMessageBox.showwarning("No file selected", "Please select a file to upload")

    def startProcessingFile(self):
        #self.processingButton = "Process file", command = self.processFile())
        self.inputFile = self.fileManager.openFile()
        self.currentFile = self.inputFile




    def processFile(self):
        fileToProcess = self.fileManager.inputFile
        if fileToProcess:
            fileAsString = self.fileToProcess.read()
            pattern = re.compile(self.textEntry.get())
            outputFileName = self.fileManager.outputFile
            outputFile = open(outputFileName, 'w+')
            outputFile.write(pattern.sub('', fileAsString))
            outputFile.close()
            viewFileButton = Button(text = "View file in text editor", command=lambda:os.system('gedit ' + outputFileName) )
            viewFileButton.place(x=50, y = 80)
            self.processingButton.configure(text = "Upload again", command=self.openFile )









def main():

        root = Tk()
        fileToProcess = None
        #window size
        root.geometry("250x150+300+300")
        app = RegExRemover(root) #this root is the parent variable
        root.mainloop()
        fileToProcess = None
        fileManager = FileManager()








if __name__ == '__main__':
    main()

