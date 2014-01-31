__author__ = 'ian.polding'

from Tkinter import Tk, Frame, BOTH, Button
import tkFileDialog

#Tk is used to create a root window
#Frame is a container for other Widgets

class Example(Frame):

    def __init__(self, parent):
        # we call the constructor of Frame - the inherited class
        Frame.__init__(self, parent, background="white")
        #we store a reference to the parent widget - in this case it is Tk root window
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Here we can set the title of the tk window
        self.parent.title("Simple")
        #pack organises widgets into vertical and horizontal boxes. It is one of three geometry managers
        #expanded in both directions
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)
        openFileButton = Button(self, text="Open a file", command=self.openFile)
        openFileButton.place(x=100, y=100)


    def openFile(self, fileToProcess):
        varName =  tkFileDialog.askopenfile('r+', title="Select file to process")
        return varName

def main():

        root = Tk()
        #window size
        root.geometry("250x150+300+300")
        app = Example(root) #this root is the parent variable
        root.mainloop()
        fileToProcess = None








if __name__ == '__main__':
    main()


















