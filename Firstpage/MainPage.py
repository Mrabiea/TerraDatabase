import tkinter as tk
import random

def setup():
    global root, output_label, choice, resultVAR

    root = tk.Tk()
    root.geometry("800x600")
    #center(root)
    root.title("Master the Database")
    # flexible_view = tk.Canvas(root, width=500, height=300,
    #                           borderwidth=2,
    #                           highlightthickness=0,
    #                           )
    # flexible_view.grid(row=0, column=1, columnspan=3)
    #insertionFields()
    insert_button = tk.Button(root, text="Insert", width=12)
    insert_button.grid(row=7, column=3, padx=20, pady=20)
    #insert_button.bind('<Button-1>', insert)
    clear_button = tk.Button(root, text="Clear", width=12)
    clear_button.grid(row=7, column=2, padx=20, pady=20)
    #clear_button.bind('<Button-1>', clear)

    resultVAR = tk.StringVar(root)
    resultVAR.set("................")
    result_label = tk.Label(root, textvariable=resultVAR, width=40)
    result_label.grid(row=8, column=1)


if __name__ == "__main__":
    setup()
    root.mainloop()