import tkinter as tk
class TerminalFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 12)

		tk.Frame.__init__(self, parent, bg="white")
		self.pack(fill="both", expand=True)
		self.makeWidgets()

		self.text = ''

	def makeWidgets(self):

		self.topFrame = tk.Frame(self)

		self.scrollbar  = tk.Scrollbar(self.topFrame)
		self.scrollbar.pack(side="right", fill="y")

		self.textArea = tk.Text(self.topFrame, bg="black", fg="green", font=self.fontMedium, yscrollcommand=self.scrollbar.set)
		self.textArea.pack(side="left", expand=True, fill="both")

		self.scrollbar.config(command=self.textArea.yview)

		self.entryFieldTextVar = tk.StringVar()
		self.entryFieldTextVar.set("")
		self.entryField = tk.Entry(self, bg="white", fg="black", font=self.fontMedium, textvariable=self.entryFieldTextVar)

		self.entryField.pack(fill="x", side="bottom")
		self.topFrame.pack(side="top", fill="both", expand=True)

		self.entryField.bind('<Return>', self.handleEnterCommand)

	def setGC(self, gc):
		self.gameController = gc

	def setTextInput(self, text):
		self.textArea.delete(1.0,"end")
		self.textArea.insert(1.0, text)

	def handleReceiveOutput(self, message, application):
		print("This adds the message to the console")
		self.text += str(application) + '> ' + str(message) + '\n'
		self.setTextInput(self.text)

	def handleEnterCommand(self, event):
		print("Command has been entered")
		response = self.entryField.get()
		self.entryField.delete(0, 'end')
		self.handleReceiveOutput(response, "console")
		print(response)
		self.gameController.updateGame(response)
