import tkinter as tk

class TerminalFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 14)

		tk.Frame.__init__(self, parent, bg="red")
		self.pack(fill="both", expand=True)
		self.makeWidgets()

	def makeWidgets(self):

		textArea = tk.Text(self, bg="black", fg="green", font=self.fontMedium)

		entryFieldTextVar = tk.StringVar()
		entryFieldTextVar.set("c:/reveille/home>")
		entryField = tk.Entry(self, bg="black", fg="green", font=self.fontMedium, textvariable=entryFieldTextVar)

		entryField.pack(fill="x", side="bottom")
		textArea.pack(side="top", fill="both", expand=True)

