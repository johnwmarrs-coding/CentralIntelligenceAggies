#Main application to test image viewer

import tkinter as tk
from tkinter import ttk
import TerminalFrame as tf
import ChatFrame as cf
import ServerFrame as sf

root = tk.Tk()
root.geometry("800x500")
root.title("Central Intelligence Aggies")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
terminalFrame = tf.TerminalFrame(tab1)

tab2 = ttk.Frame(tabControl)
chatFrame = cf.ChatFrame(tab2)

tab3 = ttk.Frame(tabControl)
serverFrame = sf.ServerFrame(tab3)

tabControl.add(tab1, text='Terminal')
tabControl.add(tab2, text='Chat Room')
tabControl.add(tab3, text='Server Traffic')

tabControl.pack(fill="both", expand=True)

root.mainloop()
