#Main application to test image viewer

import tkinter as tk
from tkinter import ttk
import TerminalFrame as tf
import ChatFrame as cf
import ServerFrame as sf
import GameController as gc

# CREATE THE CHALLENGE VARIABLE
gameController = gc.GameController()

root = tk.Tk()
root.geometry("800x500")
root.title("Central Intelligence Aggies")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
terminalFrame = tf.TerminalFrame(tab1)
terminalFrame.setGC(gameController)

tab2 = ttk.Frame(tabControl)
chatFrame = cf.ChatFrame(tab2)
chatFrame.setGC(gameController)

tab3 = ttk.Frame(tabControl)
serverFrame = sf.ServerFrame(tab3)
serverFrame.setGC(gameController)

gameController.setTerminalFrame(terminalFrame)
gameController.setChatFrame(chatFrame)
gameController.setServerFrame(serverFrame)

tabControl.add(tab1, text='Terminal')
tabControl.add(tab2, text='Chat Room')
tabControl.add(tab3, text='Server Traffic')

tabControl.pack(fill="both", expand=True)

gameController.startGame()

root.mainloop()

