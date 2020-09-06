import tkinter as tk

class TerminalFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 14)

		tk.Frame.__init__(self, parent, bg="white")
		self.pack(fill="both", expand=True)
		self.makeWidgets()

	def makeWidgets(self):

		self.topFrame = tk.Frame(self)

		self.scrollbar  = tk.Scrollbar(self.topFrame)
		self.scrollbar.pack(side="right", fill="y")

		self.textArea = tk.Text(self.topFrame, bg="black", fg="green", font=self.fontMedium, yscrollcommand=self.scrollbar.set)
		self.textArea.pack(side="left", expand=True, fill="both")

		self.scrollbar.config(command=self.textArea.yview)

		self.entryFieldTextVar = tk.StringVar()
		self.entryFieldTextVar.set("c:/reveille/home>")
		self.entryField = tk.Entry(self, bg="black", fg="green", font=self.fontMedium, textvariable=self.entryFieldTextVar)

		self.entryField.pack(fill="x", side="bottom")
		self.topFrame.pack(side="top", fill="both", expand=True, pady=(0, 5))

