import tkFileDialog

class FileManager(object):

    def __init__(self):
        self.inputFile
        self.outputFile

    def openFile(self):
        """ This acts as the setter of the filename property using tkinter's browse dialog """
        self.inputFile =  tkFileDialog.askopenfile('r+', title="Select file to process")


    def saveFile(self):
        """ This acts as the setter of the filename property using tkinter's browse dialog """
        self.outputFile = tkFileDialog.asksaveasfilename()






