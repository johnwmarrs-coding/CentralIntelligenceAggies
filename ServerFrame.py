import tkinter as tk
from tkinter import ttk

class ServerFrame(tk.Frame):

	data = [("123.23.242.21", 3), ("234.42.123.11", 7), ("124.33.421.23", 4)]
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

		self.bottomFrame = ttk.Frame(self)

		self.labelVar = tk.StringVar()
		self.labelVar.set("No Alerts at this Time")
		self.alertLabel = tk.Label(self.bottomFrame, textvariable=self.labelVar, fg="green")

		self.alertLabel.pack(side="top", fill="x", expand=True)

		self.blackListButton = tk.Button(self.bottomFrame, text="Blacklist IP", command=self.handleBlacklist)
		self.blackListButton.pack(side="bottom", fill="x")


		self.bottomFrame.pack(fill="both", side="bottom", expand=False)
		self.topFrame.pack(side="top", fill="both", expand=True)

	def setGC(self, gc):
		self.gameController = gc

	def handleBlacklist(self):
		value = self.listBox.get("active")

		actualIp = value.split(" ")[1]
		print(actualIp)

		self.gameController.updateGame(actualIp)

	def setAlert(self, message, color):
		print("Setting alert")
		self.labelVar.set(message)
		self.alertLabel.configure(text=color)

	def setIps(self, ipsAndTraffic):
		self.data = ipsAndTraffic
		self.clearIps()
		for i in range(0, len(ipsAndTraffic)):
			self.listBox.insert("end", ("IP: " + self.data[i][0] + " # requests in last hour = " + str(self.data[i][1])))

	def clearIps(self):
		self.listBox.delete(0, 'end')
