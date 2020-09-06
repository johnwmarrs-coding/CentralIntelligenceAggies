import tkinter as tk
from tkinter import ttk

class ChatFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 12)

		tk.Frame.__init__(self, parent)
		self.pack(fill="both", expand=True)
		self.makeWidgets()
		self.text = ""

	def makeWidgets(self):

		self.topFrame = tk.Frame(self)

		self.scrollbar  = tk.Scrollbar(self.topFrame)
		self.scrollbar.pack(side="right", fill="y")

		self.textArea = tk.Text(self.topFrame, bg="white", fg="black", font=self.fontMedium, yscrollcommand=self.scrollbar.set)
		self.textArea.pack(side="left", expand=True, fill="both")

		self.scrollbar.config(command=self.textArea.yview)

		self.bottomFrame = tk.Frame(self)


		self.entryFieldTextVar = tk.StringVar()
		self.entryFieldTextVar.set("")
		self.entryField = tk.Entry(self.bottomFrame, bg="white", fg="black", font=self.fontMedium, textvariable=self.entryFieldTextVar)


		self.messageLabel = ttk.Label(self.bottomFrame, text="Enter Message: ")
		self.submitButton = ttk.Button(self.bottomFrame, text="Send",command=self.handleSendMessage)
		self.submitButton.pack(fill="x", expand=True)

		self.messageLabel.pack(side="left")
		self.entryField.pack(side="right", fill="x", expand=True)
		self.submitButton.pack( side="right")

		self.bottomFrame.pack(side="bottom", fill="x", expand=False)
		self.topFrame.pack(side="top", fill="both", expand=True, pady=(0, 5))

	def handleSendMessage(self):
		print('Message Handled')
		self.handleReceiveMessage(self.entryField.get(), "Me")
		self.gameController.updateGame(self.entryField.get())

	def setGC(self, gc):
		self.gameController = gc

	def handleReceiveMessage(self, message, sender):
		print("This addes the message to the text box")
		self.text += str(sender) + ' : ' + str(message) + '\n\n'
		self.setTextInput(self.text)

	def setTextInput(self, text):
		self.textArea.delete(1.0,"end")
		self.textArea.insert(1.0, text)




