import tkinter as tk #import gui

from tkinter import *
import os

count=0 #counter to show whose go it is
player="O" #shows the text of the player
end=0 #shows if someone has won

comment=["Player O's turn", "Player X's turn"] #text to show whose go it is
com=["Player O wins","Player X wins","It's a draw"] #shows final comment

TL="" #shows text held in boxes
#same for rest of the boxes
TM=""
TR=""
ML=""
MM=""
MR=""
BL=""
BM=""
BR=""




root = tk.Tk() #loops through gui
def texton(): #resets the game
    global comment,count, txt,player,end,TL,TR,TM,ML,MM,MR,BL,BM,BR
    count = 0
    player = "O"
    end = 0
    txt.configure(text="Player O's turn")
    tl.configure(text = "   ")
    tm.configure(text = "   ")
    tr.configure(text = "   ")
    ml.configure(text = "   ")
    mm.configure(text = "   ")
    mr.configure(text = "   ")
    bl.configure(text = "   ")
    bm.configure(text = "   ")
    br.configure(text = "   ")
    TL = ""
    TM = ""
    TR = ""
    ML = ""
    MM = ""
    MR = ""
    BL = ""
    BM = ""
    BR = ""



def endo(): #prevents new inputs if someone has won
    global comment, count, txt,player
    if end == 1: #if someone has won
        change() #activates change function
        txt = tk.Button(root, text=com[count % 2], height=5, width=35, command=texton) #changes text on reset button
        txt.grid(row=3, columnspan=3)
        player="   " #sets player to blank to prevent changing of text

    elif end == 2: #if it was a draw
        txt = tk.Button(root, text=com[2], height=5, width=35, command=texton) #changes text on reset button
        txt.grid(row=3, columnspan=3)


def ending(): #checks if someone has won

    global end
    if TL == TM and TL == TR and TM != "": #checks that top row is all the same and not empty
        end = 1 #changes so someone has won
    #repeats for all winning positions
    elif ML == MM and ML == MR and ML != "":
        end = 1
    elif BL == BM and BL == BR and BL != "":
        end = 1
    elif TL == ML and TL == BL and TL != "":
        end = 1
    elif TM == MM and TM == BM and TM != "":
        end = 1
    elif TR == MR and TR == BR and TR != "":
        end = 1
    elif TL == MM and TL == BR and TL != "":
        end = 1
    elif TR == MM and TR == BL and TR != "":
        end = 1
    elif count==9: #checks if all positions have been taken showing no one has won
        end = 2 #changes to show a draw

    endo() #changes values if game is over



app = tk.Frame(root) #loops through gui
app.grid() #creates a grid


def change(): #changes whose go it is
    global player,count
    count=count+1 #increases go counter
    txt.configure(text=comment[count % 2])
    if player=="O": #checks who just went
        player = "X" #changes next player
    else:
        player="O"



def locatetl(): #changes Top Left box if pressed
    global tl,TL
    if TL=="": #checks if it is empty
        tl.configure(text=player) #changes text in box
        change() #changes next player
        TL=player #changes vlue in TL variable
        ending() #checks if someone has won
#repeat for all boxes

def locatetm():
    global tm,TM
    if TM == "":
        tm.configure(text=player)
        change()
        TM=player
        ending()

def locatetr():
    global tr,TR
    if TR == "":
        tr.configure(text=player)
        change()
        TR=player
        ending()


def locateml():
    global ml,ML
    if ML == "":
        ml.configure(text=player)
        change()
        ML=player
        ending()

def locatemm():
    global mm,MM
    if MM == "":
        mm.configure(text=player)
        change()
        MM=player
        ending()

def locatemr():
    global mr,MR
    if MR == "":
        mr.configure(text=player)
        change()
        MR=player
        ending()


def locatebl():
    global bl,BL
    if BL == "":
        bl.configure(text=player)
        change()
        BL=player
        ending()

def locatebm():
    global bm,BM
    if BM == "":
        bm.configure(text=player)
        change()
        BM=player
        ending()

def locatebr():
    global br,BR
    if BR == "":
        br.configure(text=player)
        change()
        BR=player
        ending()

txt = tk.Button(root, text = comment[count%2], height = 5, width = 35, command=texton) #defines all buttons
txt.grid(row = 3, columnspan = 3)

tl = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatetl)
tl.grid(row = 0, column = 0, ipadx = 20, ipady = 18, padx = 10, pady = 10)

tm = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatetm)
tm.grid(row = 0, column = 1, ipadx = 20, ipady = 18, padx = 10, pady = 10)

tr = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatetr)
tr.grid(row = 0, column = 2, ipadx = 20, ipady = 18, padx = 10, pady = 10)


ml = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locateml)
ml.grid(row = 1, column = 0, ipadx = 20, ipady = 18, padx = 10, pady = 10)

mm = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatemm)
mm.grid(row = 1, column = 1, ipadx = 20, ipady = 18, padx = 10, pady = 10)

mr = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatemr)
mr.grid(row = 1, column = 2, ipadx = 20, ipady = 18, padx = 10, pady = 10)


bl = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatebl)
bl.grid(row = 2, column = 0, ipadx = 20, ipady = 18, padx = 10, pady = 10)

bm = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatebm)
bm.grid(row = 2, column = 1, ipadx = 20, ipady = 18, padx = 10, pady = 10)

br = tk.Button(root, text="   ", padx=10, pady=10, fg="black", bg="white", command=locatebr)
br.grid(row = 2, column = 2, ipadx = 20, ipady = 18, padx = 10, pady = 10)

root.mainloop() #repeats