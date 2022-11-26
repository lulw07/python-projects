import tkinter as tk
import random

import setuptools

root = tk.Tk()

root.geometry("600x400")

name_var = tk.StringVar()


class random():
    list = ["rock", "paper", "scissor"]
    pc = random.choice(list)


name = str


def submit():
    global name
    name = name_var.get()
    # name_var.set("")


ai = random.pc

def test(player, ai):
    if player == ai:
        print("same")
        same_label = tk.Label(root, text="You got the same!", font=('calibre', 10, 'bold'))
        same_label.grid(row=2, column=2)
        # Quit Button
        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)

    elif player == "rock" and ai == "scissor":
        won_label = tk.Label(root, text="You won!", font=("calibre", 10, "bold"))
        won_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)


    elif player == "paper" and ai == "rock":
        won_label = tk.Label(root, text="You won!", font=("calibre", 10, "bold"))
        won_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)


    elif player == "scissor" and ai == "paper":
        won_label = tk.Label(root, text="You won!", font=("calibre", 10, "bold"))
        won_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)

    elif player == "rock" and ai == "paper":
        losse_label = tk.Label(root, text="The PC won!", font=("calibre", 10, "bold"))
        losse_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)


    elif player == "paper" and ai == "scissor":
        losse_label = tk.Label(root, text="The PC won!", font=("calibre", 10, "bold"))
        losse_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)

    elif player == "scissor" and ai == "rock":
        losse_label = tk.Label(root, text="The PC won!", font=("calibre", 10, "bold"))
        losse_label.grid(row=2, column=2)

        quit_btn = tk.Button(root, text='Quit', command=lambda: root.destroy(), font=('calibre', 10, 'normal'))
        quit_btn.grid(row=4, column=1)

def_label = tk.Label(root, text="You can select between rock, paper, scissor!", font=("calibre", 10, "normal"))

name_label = tk.Label(root, text='Input', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
show_btn = tk.Button(root, text='Show', command=lambda : test(player=name, ai=ai))



spacer1 = tk.Label(root, text="")
spacer1.grid(row=1, column=0)

def_label.grid(row=0, column=2)
name_label.grid(row=2, column=0)
name_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=1)
show_btn.grid(row=4, column=1)

root.mainloop()
