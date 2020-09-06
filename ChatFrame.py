import tkinter as tk
from tkinter import ttk

class ChatFrame(tk.Frame):
	def __init__(self, parent=None):
		self.fontMedium = ('Verdana', 14)

		tk.Frame.__init__(self, parent)
		self.pack(fill="both", expand=True)
		self.makeWidgets()

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

		self.bottomFrame.pack(side="bottom", fill="x", expand=True)
		self.topFrame.pack(side="top", fill="both", expand=True, pady=(0, 5))

	def handleSendMessage(self):
		print('Message Handled')

	def receiveMessage(self, message):
		print("This addes the message to the text box")

