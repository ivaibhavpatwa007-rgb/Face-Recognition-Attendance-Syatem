from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.reometry("1550x800+0+0")
        self.root.title("face Recognition System")





        if __name__== "__main__":
            root=Tk()
            obj=Face_Recognition_System(root)
            root.mainloop