from tkinter import ttk
import tkinter as tk
import DatabaseConnectivity.Database_access as access

# a function is required so getting the information will be easier when the
#window appears

def getting_land_info():
    pass

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def setup():
    global root
    root = tk.Tk()
    root.geometry("800x600")
    center(root)
    root.title("M&Y Project")
    land_label=ttk.Label(root,text="asdf",)
    land_label.config(font=("Courier", 44))
    land_label.grid(row=1)

if __name__ == "__main__":
    setup()
    root.mainloop()