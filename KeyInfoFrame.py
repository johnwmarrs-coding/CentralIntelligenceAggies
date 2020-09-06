import tkinter as tk
from tkinter import ttk

class KeyInfoFrame(tk.Frame):

	data = []
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 12)

		tk.Frame.__init__(self, parent, bg="white")
		self.pack(fill="both", expand=True)

		self.makeWidgets()

	def makeWidgets(self):


		self.topFrame = tk.Frame(self)

		self.scrollbar = tk.Scrollbar(self.topFrame)
		self.scrollbar.pack(side="right", fill="y")

		self.listBox = tk.Listbox(self.topFrame, yscrollcommand=self.scrollbar.set)

		for line in range(0, len(self.data)):
			self.listBox.insert("end", ("IP: " + self.data[line][0] + " # requests in last hour = " + str(self.data[line][1])))

		self.listBox.pack(side="left", fill="both", expand=True)
		self.scrollbar.config(command=self.listBox.yview)

		self.topFrame.pack(side="top", fill="both", expand=True)

	def setGC(self, gc):
		self.gameController = gc


	def clearInfo(self):
		self.listBox.delete(0, 'end')

	def addKeyInfo(self, info):
		self.data.append(info)
		self.clearInfo()
		
		for i in range(0, len(self.data)):
			self.listBox.insert("end", self.data[i])