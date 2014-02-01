__author__ = 'ian.polding'

from Tkinter import Tk, Frame, BOTH, Button, Entry, Label
import tkFileDialog
import re
import os

class Example(Frame):

    processingButton = Button

    def __init__(self, parent):
        # we call the constructor of Frame - the inherited class
        Frame.__init__(self, parent, background="white")
        #we store a reference to the parent widget - in this case it is Tk root window
        self.fileName = None
        self.parent = parent
        self.regularExpressionString = None
        self.initUI()





    def initUI(self):
        # Here we can set the title of the tk window
        self.parent.title("RegEx Remover")
        #pack organises widgets into vertical and horizontal boxes. It is one of three geometry managers
        #expanded in both directions
        self.pack(fill=BOTH, expand=1)
        self.processingButton = Button(text = "Open file", command=self.openFile)
        self.processingButton.place(x=50, y=50)


    def openFile(self):
        self.fileToProcess =  tkFileDialog.askopenfile('r+', title="Select file to process")
        self.processingButton.configure(text = "Remove Expression", command=self.processFile)
        fileBeingProcessed = Entry(cursor="dot")
        fileBeingProcessed.insert(0, self.fileToProcess.name)
        fileBeingProcessed.place(x = 0, y = 0)
        self.textEntry = Entry(cursor="dot")
        self.regexLabel = Label(text="Enter regex to remove: ")
        self.regexLabel.place(x=50, y = 10)
        self.textEntry.place(x=50, y=30)
        return self.fileToProcess

    def processFile(self):
        if self.fileToProcess:
            fileAsString = self.fileToProcess.read()
            pattern = re.compile(self.textEntry.get())
            outputFileName = tkFileDialog.asksaveasfilename()
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
        app = Example(root) #this root is the parent variable
        root.mainloop()
        fileToProcess = None








if __name__ == '__main__':
    main()

