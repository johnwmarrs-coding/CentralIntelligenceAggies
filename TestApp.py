#Main application to test image viewer

import tkinter as tk
import ImageViewer as iv
root = tk.Tk()
root.geometry("500x500")

viewer = iv.ImageViewerFrame(root)

root.mainloop()
