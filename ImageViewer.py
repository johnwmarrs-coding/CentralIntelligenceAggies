import tkinter as tk

class ImageViewerFrame(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.configure(bg="#FFFFFF")
        self.pack(side="top", fill="both", expand="true")
        self.canvas = None
        self.hbar = None
        self.vbar = None
        self.image = None
        self.zoom = 1.0

        self.prepareCanvas()
        self.canvas.bind_all("<MouseWheel>", self.handleMouseWheel)
        self.loadImage('texas.png')


    def loadImage(self, filename):
        self.image = tk.PhotoImage(file=filename)
        self.prepareCanvas()

    def prepareCanvas(self):
        #destroy the current
        if (self.canvas != None):
            self.canvas.destroy()
            self.hbar.destroy()
            self.vbar.destroy()

        self.canvas = tk.Canvas(self, bg="#FFFFFF")

        self.canvas.create_image(0, 0, anchor="nw", image=self.image)

        self.hbar = tk.Scrollbar(self, orient="horizontal")
        self.hbar.pack(side="bottom", fill="x")
        self.hbar.config(command=self.canvas.xview)

        self.vbar = tk.Scrollbar(self, orient="vertical")
        self.vbar.pack(side="right", fill="y")
        self.vbar.config(command=self.canvas.yview)

        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.pack(side="top", fill="both", expand="true")

    def zoomOut(self):
        #relout image, then zoom to preserve quality
        if (self.zoom/2.0 >= 1):
            self.zoom = self.zoom / 2.0
            self.image = self.image.subsample(2)
            self.prepareCanvas()


    def zoomIn(self):
        #Reload image, then zoom to preserve quality
        if (self.zoom * 2 <= 5):
            self.zoom = self.zoom * 2.0
            self.image = self.image.zoom(2)
            self.prepareCanvas()

    def handleMouseWheel(self, event):
        print(event.delta)
        if (event.delta > 0):
            self.zoomIn()
        elif (event.delta < 0):
            self.zoomOut()
