import tkinter as tk

class ServerFrame(tk.Frame):

	data = [("123.23.242.21", 3), ("234.42.123.11", 7), ("124.33.421.23", 4)]
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 14)

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

		self.bottomFrame = tk.Frame(self)

		self.bottomFrame.pack(fill="both", side="bottom", expand=True)
		self.topFrame.pack(side="top", fill="both", expand=True)