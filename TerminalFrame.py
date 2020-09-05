import tkinter as tk

class TerminalFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 14)

		tk.Frame.__init__(self, parent, bg="white")
		self.pack(fill="both", expand=True)
		self.makeWidgets()

	def makeWidgets(self):

		topFrame = tk.Frame(self)

		scrollbar  = tk.Scrollbar(topFrame)
		scrollbar.pack(side="right", fill="y")

		textArea = tk.Text(topFrame, bg="black", fg="green", font=self.fontMedium, yscrollcommand=scrollbar.set)
		textArea.pack(side="left", expand=True, fill="both")

		scrollbar.config(command=textArea.yview)

		entryFieldTextVar = tk.StringVar()
		entryFieldTextVar.set("c:/reveille/home>")
		entryField = tk.Entry(self, bg="black", fg="green", font=self.fontMedium, textvariable=entryFieldTextVar)

		entryField.pack(fill="x", side="bottom")
		topFrame.pack(side="top", fill="both", expand=True, pady=(0, 5))

