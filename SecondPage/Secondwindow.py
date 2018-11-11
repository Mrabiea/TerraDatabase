from tkinter import ttk
import tkinter as tk
import Firstpage.MainPage as main
import DatabaseConnectivity.Database_access as access


# a function is required so getting the information will be easier when the
# window appears

def getting_land_info(land):
    land_list = access.getlandinfo(land)
    return land_list


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def newwindow():
    global secondroot
    # land_information=
    secondroot = tk.Toplevel(main.root)
    #root.geometry("800x600")
    center(secondroot)
    secondroot.title("M&Y Project")
    land_info = getting_land_info("Österreich")
    land_label = ttk.Label(secondroot, text=land_info[0][1], justify=tk.CENTER)
    land_label.configure(font=("Calibri", 22))
    land_label.place(relx=0.25)
    land_label.grid(row=0, column=1)

    scrollbar = tk.Scrollbar(secondroot)

    citys_label = ttk.Label(secondroot, text="Citys of " + land_info[0][1])
    citys_label.grid(row=1, column=1)
    informations = tk.Listbox(secondroot, width=30)
    informations.grid(row=2, column=1, columnspan=1, padx=10)
    informations.config(yscrollcommand=scrollbar.set)
    informations.bind("<B1-Leave>", lambda event: "break")

    for i in access.getcities("österreich"):
        informations.insert(tk.END, i)
    secondroot.mainloop()



