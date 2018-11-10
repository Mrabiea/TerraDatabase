import tkinter as tk
from tkinter import ttk
import DatabaseConnectivity.Database_access as access
import itertools


def setup():
    global root
    root = tk.Tk()
    root.title("M&Y project")

    continent_L = ttk.Label(root, text="Choose a continent:", width=20)
    continent_L.grid(row=0, column=0, padx=20, pady=20)
    country_L = ttk.Label(root, text="Choose a country:", width=20)
    country_L.grid(row=1, column=0, padx=20, pady=20)
    # hier gab einen Fehler weil die liste hatte mehrere listen drin so ist gelöst. Rabiea
    continent = [item for sublist in access.getallContinent() for item in sublist]
    # OptionMenu braucht eine verändbare Varibale deshalb habe ich sie hinzugefügt
    string=tk.StringVar()
    continent_C = ttk.OptionMenu(root,string,*continent)
    continent_C.config(width=20)
    continent_C.grid(row=0, column=1, padx=20, pady=20)
    country_C = ttk.OptionMenu(root, 'Choose a country')
    country_C.config(width=20)
    country_C.grid(row=1, column=1, padx=20, pady=20)

    go = ttk.Button(root, text='Go!', width=20)
    go.grid(row=2, column=1, padx=20, pady=20)


if __name__ == '__main__':
    access.connectto_database()
    setup()
    root.mainloop()
