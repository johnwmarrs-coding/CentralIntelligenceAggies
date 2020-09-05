#Main application to test image viewer

import tkinter as tk
from tkinter import ttk
import TerminalFrame as tf

root = tk.Tk()
root.geometry("800x500")
root.title("Central Intelligence Aggies")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)

terminalFrame = tf.TerminalFrame(tab1)

tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Terminal')
tabControl.add(tab2, text='Email')

tabControl.pack(fill="both", expand=True)

root.mainloop()
