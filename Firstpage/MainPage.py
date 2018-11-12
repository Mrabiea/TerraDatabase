import tkinter as tk
from tkinter import ttk
import DatabaseConnectivity.Database_access as access


def getting_land_info(land):
    land_list = access.getlandinfo(land)
    return land_list


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    # (win.winfo_screenheight() // 2) -

def popupmsg(message):
    global root
    popup = tk.Toplevel()
    popup.wm_title("!caution")
    center(popup)
    label = ttk.Label(popup, text=message)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()




def selecteditem(*args):
    popupmsg("jaaa")

def newwindow():
    global secondroot, root, countries_string, contient_string

    secondroot = tk.Toplevel(root)
    secondroot.geometry("800x600")
    center(secondroot)
    secondroot.title("M&Y Project")
    land_info = getting_land_info(countries_string.get())
    land_label = ttk.Label(secondroot, text=land_info[0][1], justify=tk.CENTER)
    land_label.configure(font=("Calibri", 22))
    land_label.place(relx=0.25)
    land_label.grid(row=0, column=2)

    scrollbar = tk.Scrollbar(secondroot)
    continent_label = ttk.Label(secondroot, text="Continent: " + contient_string.get())
    continent_label.configure(font=("Calibri", 18))
    continent_label.grid(row=1, column=2)

    capital_city_label = ttk.Label(secondroot, text="The Capital: " + land_info[0][5])
    capital_city_label.configure(font=("Calibri", 18))
    capital_city_label.grid(row=2, column=2)

    cities_label = ttk.Label(secondroot, text="Cities of " + land_info[0][1])
    cities_label.grid(row=3, column=1)
    city_list = tk.Listbox(secondroot, width=30)
    city_list.grid(row=4, column=1, columnspan=1, padx=10)
    city_list.config(yscrollcommand=scrollbar.set)
    city_list.bind("<<ListboxSelect>>", selecteditem)

    for i in access.getcities(countries_string.get()):
        if i[1] is not None:
            city_list.insert(tk.END, i[0] + "-->" + i[1])
        else:
            city_list.insert(tk.END, i[0])

    neighborlands = tk.Label(secondroot, text="Neighbors of " + land_info[0][1])
    neighborlands.grid(row=3, column=2)
    neighborlands_list = tk.Listbox(secondroot)
    neighborlands_list.grid(row=4, column=2, columnspan=1, padx=10)
    neighborlands_list.bind("<B1-Leave>", lambda event: "break")

    for i in access.getneighborland(countries_string.get()):
        neighborlands_list.insert(tk.END, i)

    languages = tk.Label(secondroot, text="Languages spoken in " + land_info[0][1])
    languages.grid(row=3, column=3, padx=10)
    languages_list = tk.Listbox(secondroot)
    languages_list.grid(row=4, column=3, padx=10)
    for i in access.getlanguage(countries_string.get()):
        languages_list.insert(tk.END, i)
    secondroot.mainloop()


def selectedContinent(*args):
    global country_list, contient_string, country_C
    country_list = [item for sublist in access.getalllands(contient_string.get()) for item in
                    sublist]
    country_C.set_menu(*country_list)


def enabelingButton(*args):
    global go
    go.configure(state="normal")


def setup():
    global root, counrties_string, contient_string, country_list, country_C, countries_string, go
    root = tk.Tk()
    root.title("M&Y project")
    root.geometry("600x400")
    center(root)
    continent_L = ttk.Label(root, text="Choose a continent:", width=20)
    continent_L.grid(row=0, column=0, padx=20, pady=20)
    country_L = ttk.Label(root, text="Choose a country:", width=20)
    country_L.grid(row=1, column=0, padx=20, pady=20)
    # hier gab einen Fehler weil die liste hatte mehrere listen drin so ist gelöst. Rabiea
    continent = [item for sublist in access.getallContinent() for item in sublist]
    # OptionMenu braucht eine verändbare Varibale deshalb habe ich sie hinzugefügt
    contient_string = tk.StringVar()

    continent_C = ttk.OptionMenu(root, contient_string, "Choose a Continent",
                                 *continent, command=selectedContinent)
    continent_C.config(width=20)
    continent_C.grid(row=0, column=1, padx=20, pady=20)

    country_list = []
    countries_string = tk.StringVar()
    country_C = ttk.OptionMenu(root, countries_string, 'Choose a country')
    country_C.config(width=20)
    country_C.grid(row=1, column=1, padx=20, pady=20)
    countries_string.trace("w", enabelingButton)

    go = ttk.Button(root, text='Go!', width=20, command=newwindow)
    go.configure(state="disabled")
    go.grid(row=2, column=1, padx=20, pady=20)
    # go.bind('<Button-1>', func=newwindow)


if __name__ == "__main__":
    access.connectto_database()
    setup()
    root.mainloop()
