from tkinter import tkfiledialog

class FileManager:
	
	def __init__(self):
		self.filename
		
	def openFile(self):
	""" This acts as the setter of the filename property using tkinter's browse dialog """
		self.filename = tkfiledialog.saveas
		