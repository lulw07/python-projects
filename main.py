import random
import tkinter as tk
from tkinter import *

### Start GUI

root = tk.Tk()

root.geometry("600x400")

name_var = tk.StringVar()


def submit():
    global choose
    choose = name_var.get()
    name_var.set("")


list = ["rock", "paper", "scissor"]
pc = random.choice(list)

name_label = tk.Label(root, text='Input', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
show = tk.Button(root, text='Show', command=lambda: test(player=choose, pc=pc), font=('calibre', 10, 'normal'))
won_label = tk.Label(root, text="Player won the game!", font=('calibre', 10, 'bold'))
loose_label = tk.Label(root, text="PC won the game!", font=('calibre', 10, 'bold'))
player_won = False
pc_won = False


def test(player, pc):
    if player == "rock" and pc == "scissor":
        player_won == True
        return player_won

    elif player == "paper" and pc == "rock":
        player_won == True
        return player_won

    elif player == "scissor" and pc == "paper":
        player_won == True
        return player_won

    elif player == "rock" and pc == "paper":
        pc_won == True
        return pc_won

    elif player == "paper" and pc == "scissor":
        pc_won == True
        return pc_won

    elif player == "scissor" and pc == "rock":
        pc_won == True
        return pc_won




if player_won == True:
    won_label



if pc_won == True:
    loose_label



def evaluation(player, pc):
    if player != pc:
        print("You selected: ", player)
        print("The computer selected: ", pc)

    if player == pc:
        print("You got the same")



name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)
show.grid(row=3, column=1)
won_label.grid(row=4, column=1)
loose_label.grid(row=4, column=1)
root.mainloop()

### End GUI


print(pc)

print(choose)
