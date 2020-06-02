import winsound #used for sound
import tkinter as tk #used for piano board
import time #used as a timer

root = tk.Tk() #loops

def c(): #function for when c is printed
    winsound.Beep(164, 100) #emits frequency of sound for c
#same for rest of the board
def c1():
        winsound.Beep(327, 100)
def c2():
    winsound.Beep(654, 100)
def c3():
    winsound.Beep(1301, 100)


def db():
        winsound.Beep(173, 100)
def db1():
        winsound.Beep(347, 100)

def db2():
    winsound.Beep(693, 100)
def db3():
    winsound.Beep(1386, 100)


def d():
        winsound.Beep(184, 100)
def d1():
        winsound.Beep(367, 100)

def d2():
    winsound.Beep(734, 100)
def d3():
    winsound.Beep(1468, 100)


def eb():
        winsound.Beep(195, 100)
def eb1():
        winsound.Beep(389, 100)

def eb2():
    winsound.Beep(778, 100)
def eb3():
    winsound.Beep(1556, 100)


def e():
        winsound.Beep(206, 100)
def e1():
        winsound.Beep(412, 100)

def e2():
    winsound.Beep(824, 100)
def e3():
    winsound.Beep(1648, 100)


def f():
        winsound.Beep(218, 100)
def f1():
        winsound.Beep(437, 100)

def f2():
    winsound.Beep(873, 100)
def f3():
    winsound.Beep(1746, 100)


def gb():
        winsound.Beep(231, 100)
def gb1():
        winsound.Beep(463, 100)

def gb2():
    winsound.Beep(925, 100)
def gb3():
    winsound.Beep(1850, 100)


def g():
        winsound.Beep(245, 100)
def g1():
        winsound.Beep(490, 100)

def g2():
    winsound.Beep(980, 100)
def g3():
    winsound.Beep(1960, 100)


def ab():
        winsound.Beep(260, 100)
def ab1():
        winsound.Beep(519, 100)

def ab2():
    winsound.Beep(1038, 100)
def ab3():
    winsound.Beep(2077, 100)


def a():
        winsound.Beep(275, 100)
def a1():
        winsound.Beep(550, 100)

def a2():
    winsound.Beep(1100, 100)
def a3():
    winsound.Beep(2200, 100)


def bb():
        winsound.Beep(291, 100)
def bb1():
        winsound.Beep(583, 100)

def bb2():
    winsound.Beep(1165, 100)
def bb3():
    winsound.Beep(2331, 100)


def b():
        winsound.Beep(309, 100)
def b1():
        winsound.Beep(617, 100)

def b2():
    winsound.Beep(1235, 100)
def b3():
    winsound.Beep(2469, 100)



keyc = tk.Button(root, bg="white", height=10, width=7, command=c)
keyc.grid(row = 0, column = 0)

keydb = tk.Button(root, bg="black", height=10, width=5, command=db)
keydb.grid(row = 0, column = 1)

keyd = tk.Button(root, bg="white", height=10, width=7, command=d)
keyd.grid(row = 0, column = 2)

keyeb = tk.Button(root, bg="black", height=10, width=5, command=eb)
keyeb.grid(row = 0, column = 3)

keye = tk.Button(root, bg="white", height=10, width=7, command=e)
keye.grid(row = 0, column = 4)

keyf = tk.Button(root, bg="white", height=10, width=7, command=f)
keyf.grid(row = 0, column = 5)

keygb = tk.Button(root, bg="black", height=10, width=5, command=gb)
keygb.grid(row = 0, column = 6)

keyg = tk.Button(root, bg="white", height=10, width=7, command=g)
keyg.grid(row = 0, column = 7)

keyab = tk.Button(root, bg="black", height=10, width=5, command=ab)
keyab.grid(row = 0, column = 8)

keya = tk.Button(root, bg="white", height=10, width=7, command=a)
keya.grid(row = 0, column = 9)

keybb = tk.Button(root, bg="black", height=10, width=5, command=bb)
keybb.grid(row = 0, column = 10)

keyb = tk.Button(root, bg="white", height=10, width=7, command=b)
keyb.grid(row = 0, column = 11)



keyc1 = tk.Button(root, bg="white", height=10, width=7, command=c1)
keyc1.grid(row = 0, column = 12)

keydb1 = tk.Button(root, bg="black", height=10, width=5, command=db1)
keydb1.grid(row = 0, column = 13)

keyd1 = tk.Button(root, bg="white", height=10, width=7, command=d1)
keyd1.grid(row = 0, column = 14)

keyeb1 = tk.Button(root, bg="black", height=10, width=5, command=eb1)
keyeb1.grid(row = 0, column = 15)

keye1 = tk.Button(root, bg="white", height=10, width=7, command=e1)
keye1.grid(row = 0, column = 16)

keyf1 = tk.Button(root, bg="white", height=10, width=7, command=f1)
keyf1.grid(row = 0, column = 17)

keygb1 = tk.Button(root, bg="black", height=10, width=5, command=gb1)
keygb1.grid(row = 0, column = 18)

keyg1 = tk.Button(root, bg="white", height=10, width=7, command=g1)
keyg1.grid(row = 0, column = 19)

keyab1 = tk.Button(root, bg="black", height=10, width=5, command=ab1)
keyab1.grid(row = 0, column = 20)

keya1 = tk.Button(root, bg="white", height=10, width=7, command=a1)
keya1.grid(row = 0, column = 21)

keybb1 = tk.Button(root, bg="black", height=10, width=5, command=bb1)
keybb1.grid(row = 0, column = 22)

keyb1 = tk.Button(root, bg="white", height=10, width=7, command=b1)
keyb1.grid(row = 0, column = 23)






keyc2 = tk.Button(root, bg="white", height=10, width=7, command=c2)
keyc2.grid(row = 1, column = 0)

keydb2 = tk.Button(root, bg="black", height=10, width=5, command=db2)
keydb2.grid(row = 1, column = 1)

keyd2 = tk.Button(root, bg="white", height=10, width=7, command=d2)
keyd2.grid(row = 1, column = 2)

keyeb2 = tk.Button(root, bg="black", height=10, width=5, command=eb2)
keyeb2.grid(row = 1, column = 3)

keye2 = tk.Button(root, bg="white", height=10, width=7, command=e2)
keye2.grid(row = 1, column = 4)

keyf2 = tk.Button(root, bg="white", height=10, width=7, command=f2)
keyf2.grid(row = 1, column = 5)

keygb2 = tk.Button(root, bg="black", height=10, width=5, command=gb2)
keygb2.grid(row = 1, column = 6)

keyg2 = tk.Button(root, bg="white", height=10, width=7, command=g2)
keyg2.grid(row = 1, column = 7)

keyab2 = tk.Button(root, bg="black", height=10, width=5, command=ab2)
keyab2.grid(row = 1, column = 8)

keya2 = tk.Button(root, bg="white", height=10, width=7, command=a2)
keya2.grid(row = 1, column = 9)

keybb2 = tk.Button(root, bg="black", height=10, width=5, command=bb2)
keybb2.grid(row = 1, column = 10)

keyb2 = tk.Button(root, bg="white", height=10, width=7, command=b2)
keyb2.grid(row = 1, column = 11)



keyc3 = tk.Button(root, bg="white", height=10, width=7, command=c3)
keyc3.grid(row = 1, column = 12)

keydb3 = tk.Button(root, bg="black", height=10, width=5, command=db3)
keydb3.grid(row = 1, column = 13)

keyd3 = tk.Button(root, bg="white", height=10, width=7, command=d3)
keyd3.grid(row = 1, column = 14)

keyeb3 = tk.Button(root, bg="black", height=10, width=5, command=eb3)
keyeb3.grid(row = 1, column = 15)

keye3 = tk.Button(root, bg="white", height=10, width=7, command=e3)
keye3.grid(row = 1, column = 16)

keyf3 = tk.Button(root, bg="white", height=10, width=7, command=f3)
keyf3.grid(row = 1, column = 17)

keygb3 = tk.Button(root, bg="black", height=10, width=5, command=gb3)
keygb3.grid(row = 1, column = 18)

keyg3= tk.Button(root, bg="white", height=10, width=7, command=g3)
keyg3.grid(row = 1, column = 19)

keyab3 = tk.Button(root, bg="black", height=10, width=5, command=ab3)
keyab3.grid(row = 1, column = 20)

keya3 = tk.Button(root, bg="white", height=10, width=7, command=a3)
keya3.grid(row = 1, column = 21)

keybb3 = tk.Button(root, bg="black", height=10, width=5, command=bb3)
keybb3.grid(row = 1, column = 22)

keyb3 = tk.Button(root, bg="white", height=10, width=7, command=b3)
keyb3.grid(row = 1, column = 23)






root.mainloop() #loops
