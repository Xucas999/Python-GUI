import winsound #imports for sounds
import tkinter as tk #imports for gui
import time #imports a timer

root = tk.Tk() #initializes tkinter background

def e(): #function e
    winsound.Beep(412, 100) #frequency for an e
#repeats for all keys
def f():
    winsound.Beep(437, 100)
def gb():
    winsound.Beep(463, 100)
def g():
    winsound.Beep(490, 100)
def ab():
    winsound.Beep(519, 100)
def a():
        winsound.Beep(550, 100)
def bb():
    winsound.Beep(583, 100)
def b():
        winsound.Beep(617, 100)
def c():
    winsound.Beep(654, 100)
def db():
    winsound.Beep(693, 100)
def d():
        winsound.Beep(734, 100)
def eb():
    winsound.Beep(778, 100)


def e1():
        winsound.Beep(824, 100)
def f1():
    winsound.Beep(873, 100)
def gb1():
    winsound.Beep(925, 100)
def g1():
    winsound.Beep(980,100)
def ab1():
    winsound.Beep(1038, 100)
def a1():
    winsound.Beep(1100, 100)
def bb1():
    winsound.Beep(1165, 100)
def b1():
    winsound.Beep(1235, 100)

def c1():
    winsound.Beep(1308, 100)
def db1():
    winsound.Beep(1386, 100)
def d1():
    winsound.Beep(1468, 100)
def eb1():
    winsound.Beep(1556, 100)
def e2():
    winsound.Beep(1648, 100)
def f2():
    winsound.Beep(1746, 100)
def gb2():
    winsound.Beep(1850, 100)
def g2():
    winsound.Beep(1960, 100)
def ab2():
    winsound.Beep(2077, 100)
def a2():
    winsound.Beep(2200, 100)
def bb2():
    winsound.Beep(2331, 100)
def b2():
    winsound.Beep(2469, 100)
def c2():
    winsound.Beep(2616, 100)
def db2():
    winsound.Beep(2772, 100)

fret0 = tk.Button(root, text="0",bg="white", height=2, width=7) #initializes the text for all frets showing the number for the fret
fret0.grid(row = 4, column = 0) #initializes the location of the background button for all frets
#repeats for all frets

fret1 = tk.Button(root, text="1",bg="white", height=2, width=7)
fret1.grid(row = 4, column = 1)

fret2 = tk.Button(root, text="2",bg="white", height=2, width=7)
fret2.grid(row = 4, column = 2)

fret3 = tk.Button(root, text="3",bg="white", height=2, width=7)
fret3.grid(row = 4, column = 3)

fret4 = tk.Button(root, text="4",bg="white", height=2, width=7)
fret4.grid(row = 4, column = 4)

fret5 = tk.Button(root, text="5",bg="white", height=2, width=7)
fret5.grid(row = 4, column = 5)

fret6 = tk.Button(root, text="6",bg="white", height=2, width=7)
fret6.grid(row = 4, column = 6)

fret7 = tk.Button(root, text="7",bg="white", height=2, width=7)
fret7.grid(row = 4, column = 7)

fret8 = tk.Button(root, text="8",bg="white", height=2, width=7)
fret8.grid(row = 4, column = 8)

fret9 = tk.Button(root, text="9",bg="white", height=2, width=7)
fret9.grid(row = 4, column = 9)

fret10 = tk.Button(root, text="10",bg="white", height=2, width=7)
fret10.grid(row = 4, column = 10)

fret11 = tk.Button(root, text="11",bg="white", height=2, width=7)
fret11.grid(row = 4, column = 11)

fret12 = tk.Button(root, text="12",bg="white", height=2, width=7)
fret12.grid(row = 4, column = 12)

fret13 = tk.Button(root, text="13",bg="white", height=2, width=7)
fret13.grid(row = 4, column = 13)

fret14 = tk.Button(root, text="14",bg="white", height=2, width=7)
fret14.grid(row = 4, column = 14)

fret15 = tk.Button(root, text="15",bg="white", height=2, width=7)
fret15.grid(row = 4, column = 15)

fret16 = tk.Button(root, text="16",bg="white", height=2, width=7)
fret16.grid(row = 4, column = 16)

fret17 = tk.Button(root, text="17",bg="white", height=2, width=7)
fret17.grid(row = 4, column = 17)

fret18 = tk.Button(root, text="18",bg="white", height=2, width=7)
fret18.grid(row = 4, column = 18)



se = tk.Button(root, bg="white", height=2, width=7, command=e) #initializes the colour and size of the background button for all frets which show what function is activated
se.grid(row = 3, column = 0) #initializes the location of the backgroundbutton for a frets
#repeats for all frets

se1 = tk.Button(root, bg="white", height=2, width=7, command=f)
se1.grid(row = 3, column = 1)

se2 = tk.Button(root, bg="white", height=2, width=7, command=gb)
se2.grid(row = 3, column = 2)

se3 = tk.Button(root, bg="white", height=2, width=7, command=g)
se3.grid(row = 3, column = 3)

se4 = tk.Button(root, bg="white", height=2, width=7, command=ab)
se4.grid(row = 3, column = 4)

se5 = tk.Button(root, bg="white", height=2, width=7, command=a)
se5.grid(row = 3, column = 5)

se6 = tk.Button(root, bg="white", height=2, width=7, command=bb)
se6.grid(row = 3, column = 6)

se7 = tk.Button(root, bg="white", height=2, width=7, command=b)
se7.grid(row = 3, column = 7)

se8 = tk.Button(root, bg="white", height=2, width=7, command=c)
se8.grid(row = 3, column = 8)

se9 = tk.Button(root, bg="white", height=2, width=7, command=db)
se9.grid(row = 3, column = 9)

se10 = tk.Button(root, bg="white", height=2, width=7, command=d)
se10.grid(row = 3, column = 10)

se11 = tk.Button(root, bg="white", height=2, width=7, command=eb)
se11.grid(row = 3, column = 11)

se12 = tk.Button(root, bg="white", height=2, width=7, command=e1)
se12.grid(row = 3, column = 12)

se13 = tk.Button(root, bg="white", height=2, width=7, command=f1)
se13.grid(row = 3, column = 13)

se14 = tk.Button(root, bg="white", height=2, width=7, command=gb1)
se14.grid(row = 3, column = 14)

se15 = tk.Button(root, bg="white", height=2, width=7, command=g1)
se15.grid(row = 3, column = 15)

se16 = tk.Button(root, bg="white", height=2, width=7, command=ab1)
se16.grid(row = 3, column = 16)

se17 = tk.Button(root, bg="white", height=2, width=7, command=a1)
se17.grid(row = 3, column = 17)

se18 = tk.Button(root, bg="white", height=2, width=7, command=bb1)
se18.grid(row = 3, column = 18)



sa = tk.Button(root, bg="white", height=2, width=7, command=a)
sa.grid(row = 2, column = 0)

sa1 = tk.Button(root, bg="white", height=2, width=7, command=bb)
sa1.grid(row = 2, column = 1)

sa2 = tk.Button(root, bg="white", height=2, width=7, command=b)
sa2.grid(row = 2, column = 2)

sa3 = tk.Button(root, bg="white", height=2, width=7, command=c)
sa3.grid(row = 2, column = 3)

sa4 = tk.Button(root, bg="white", height=2, width=7, command=db)
sa4.grid(row = 2, column = 4)

sa5 = tk.Button(root, bg="white", height=2, width=7, command=d)
sa5.grid(row = 2, column = 5)

sa6 = tk.Button(root, bg="white", height=2, width=7, command=eb)
sa6.grid(row = 2, column = 6)

sa7 = tk.Button(root, bg="white", height=2, width=7, command=e1)
sa7.grid(row = 2, column = 7)

sa8 = tk.Button(root, bg="white", height=2, width=7, command=f1)
sa8.grid(row = 2, column = 8)

sa9 = tk.Button(root, bg="white", height=2, width=7, command=gb1)
sa9.grid(row = 2, column = 9)

sa10 = tk.Button(root, bg="white", height=2, width=7, command=g1)
sa10.grid(row = 2, column = 10)

sa11 = tk.Button(root, bg="white", height=2, width=7, command=ab1)
sa11.grid(row = 2, column = 11)

sa12 = tk.Button(root, bg="white", height=2, width=7, command=a1)
sa12.grid(row = 2, column = 12)

sa13 = tk.Button(root, bg="white", height=2, width=7, command=bb1)
sa13.grid(row = 2, column = 13)

sa14 = tk.Button(root, bg="white", height=2, width=7, command=b1)
sa14.grid(row = 2, column = 14)

sa15 = tk.Button(root, bg="white", height=2, width=7, command=c1)
sa15.grid(row = 2, column = 15)

sa16 = tk.Button(root, bg="white", height=2, width=7, command=db1)
sa16.grid(row = 2, column = 16)

sa17 = tk.Button(root, bg="white", height=2, width=7, command=d1)
sa17.grid(row = 2, column = 17)

sa18 = tk.Button(root, bg="white", height=2, width=7, command=eb1)
sa18.grid(row = 2, column = 18)


sd = tk.Button(root, bg="white", height=2, width=7, command=d)
sd.grid(row = 1, column = 0)

sd1 = tk.Button(root, bg="white", height=2, width=7, command=eb)
sd1.grid(row = 1, column = 1)

sd2 = tk.Button(root, bg="white", height=2, width=7, command=e1)
sd2.grid(row = 1, column = 2)

sd3 = tk.Button(root, bg="white", height=2, width=7, command=f1)
sd3.grid(row = 1, column = 3)

sd4 = tk.Button(root, bg="white", height=2, width=7, command=gb1)
sd4.grid(row = 1, column = 4)

sd5 = tk.Button(root, bg="white", height=2, width=7, command=g1)
sd5.grid(row = 1, column = 5)

sd6 = tk.Button(root, bg="white", height=2, width=7, command=ab1)
sd6.grid(row = 1, column = 6)

sd7 = tk.Button(root, bg="white", height=2, width=7, command=a1)
sd7.grid(row = 1, column = 7)

sd8 = tk.Button(root, bg="white", height=2, width=7, command=bb1)
sd8.grid(row = 1, column = 8)

sd9 = tk.Button(root, bg="white", height=2, width=7, command=b1)
sd9.grid(row = 1, column = 9)

sd10 = tk.Button(root, bg="white", height=2, width=7, command=c1)
sd10.grid(row = 1, column = 10)

sd11 = tk.Button(root, bg="white", height=2, width=7, command=db1)
sd11.grid(row = 1, column = 11)

sd12 = tk.Button(root, bg="white", height=2, width=7, command=d1)
sd12.grid(row = 1, column = 12)

sd13 = tk.Button(root, bg="white", height=2, width=7, command=eb1)
sd13.grid(row = 1, column = 13)

sd14 = tk.Button(root, bg="white", height=2, width=7, command=e2)
sd14.grid(row = 1, column = 14)

sd15 = tk.Button(root, bg="white", height=2, width=7, command=f2)
sd15.grid(row = 1, column = 15)

sd16 = tk.Button(root, bg="white", height=2, width=7, command=gb2)
sd16.grid(row = 1, column = 16)

sd17 = tk.Button(root, bg="white", height=2, width=7, command=g2)
sd17.grid(row = 1, column = 17)

sd18 = tk.Button(root, bg="white", height=2, width=7, command=ab2)
sd18.grid(row = 1, column = 18)




sg = tk.Button(root, bg="white", height=2, width=7, command=g1)
sg.grid(row = 0, column = 0)

sg1 = tk.Button(root, bg="white", height=2, width=7, command=ab1)
sg1.grid(row = 0, column = 1)

sg2 = tk.Button(root, bg="white", height=2, width=7, command=a1)
sg2.grid(row = 0, column = 2)

sg3 = tk.Button(root, bg="white", height=2, width=7, command=bb1)
sg3.grid(row = 0, column = 3)

sg4 = tk.Button(root, bg="white", height=2, width=7, command=b1)
sg4.grid(row = 0, column = 4)

sg5 = tk.Button(root, bg="white", height=2, width=7, command=c1)
sg5.grid(row = 0, column = 5)

sg6 = tk.Button(root, bg="white", height=2, width=7, command=db1)
sg6.grid(row = 0, column = 6)

sg7 = tk.Button(root, bg="white", height=2, width=7, command=d1)
sg7.grid(row = 0, column = 7)

sg8 = tk.Button(root, bg="white", height=2, width=7, command=eb1)
sg8.grid(row = 0, column = 8)

sg9 = tk.Button(root, bg="white", height=2, width=7, command=e2)
sg9.grid(row = 0, column = 9)

sg10 = tk.Button(root, bg="white", height=2, width=7, command=f2)
sg10.grid(row = 0, column = 10)

sg11 = tk.Button(root, bg="white", height=2, width=7, command=gb2)
sg11.grid(row = 0, column = 11)

sg12 = tk.Button(root, bg="white", height=2, width=7, command=g2)
sg12.grid(row = 0, column = 12)

sg13 = tk.Button(root, bg="white", height=2, width=7, command=ab2)
sg13.grid(row = 0, column = 13)

sg14 = tk.Button(root, bg="white", height=2, width=7, command=a2)
sg14.grid(row = 0, column = 14)

sg15 = tk.Button(root, bg="white", height=2, width=7, command=bb2)
sg15.grid(row = 0, column = 15)

sg16 = tk.Button(root, bg="white", height=2, width=7, command=b2)
sg16.grid(row = 0, column = 16)

sg17 = tk.Button(root, bg="white", height=2, width=7, command=c2)
sg17.grid(row = 0, column = 17)

sg18 = tk.Button(root, bg="white", height=2, width=7, command=db2)
sg18.grid(row = 0, column = 18)




sec = tk.Button(root, bg="black", height=1, width=7, command=e) #initializes the colour and size of the button for all frets which show what function is activated
sec.grid(row = 3, column = 0)#initializes the location of the button for a frets
#repeats for all frets

se1c = tk.Button(root, bg="black", height=1, width=7, command=f)
se1c.grid(row = 3, column = 1)

se2c = tk.Button(root, bg="black", height=1, width=7, command=gb)
se2c.grid(row = 3, column = 2)

se3c = tk.Button(root, bg="black", height=1, width=7, command=g)
se3c.grid(row = 3, column = 3)

se4c = tk.Button(root, bg="black", height=1, width=7, command=ab)
se4c.grid(row = 3, column = 4)

se5c = tk.Button(root, bg="black", height=1, width=7, command=a)
se5c.grid(row = 3, column = 5)

se7c = tk.Button(root, bg="black", height=1, width=7, command=bb)
se7c.grid(row = 3, column = 6)

se7c = tk.Button(root, bg="black", height=1, width=7, command=b)
se7c.grid(row = 3, column = 7)

se8c = tk.Button(root, bg="black", height=1, width=7, command=c)
se8c.grid(row = 3, column = 8)

se9c = tk.Button(root, bg="black", height=1, width=7, command=db)
se9c.grid(row = 3, column = 9)

se10c = tk.Button(root, bg="black", height=1, width=7, command=d)
se10c.grid(row = 3, column = 10)

se11c = tk.Button(root, bg="black", height=1, width=7, command=eb)
se11c.grid(row = 3, column = 11)

se12c = tk.Button(root, bg="black", height=1, width=7, command=e1)
se12c.grid(row = 3, column = 12)

se13c = tk.Button(root, bg="black", height=1, width=7, command=f1)
se13c.grid(row = 3, column = 13)

se14c = tk.Button(root, bg="black", height=1, width=7, command=gb1)
se14c.grid(row = 3, column = 14)

se15c = tk.Button(root, bg="black", height=1, width=7, command=g1)
se15c.grid(row = 3, column = 15)

se16c = tk.Button(root, bg="black", height=1, width=7, command=ab1)
se16c.grid(row = 3, column = 16)

se17c = tk.Button(root, bg="black", height=1, width=7, command=a1)
se17c.grid(row = 3, column = 17)

se18c = tk.Button(root, bg="black", height=1, width=7, command=bb1)
se18c.grid(row = 3, column = 18)



sac = tk.Button(root, bg="black", height=1, width=7, command=a)
sac.grid(row = 2, column = 0)

sa1c = tk.Button(root, bg="black", height=1, width=7, command=bb)
sa1c.grid(row = 2, column = 1)

sa2c = tk.Button(root, bg="black", height=1, width=7, command=b)
sa2c.grid(row = 2, column = 2)

sa3c = tk.Button(root, bg="black", height=1, width=7, command=c)
sa3c.grid(row = 2, column = 3)

sa4c = tk.Button(root, bg="black", height=1, width=7, command=db)
sa4c.grid(row = 2, column = 4)

sa5c = tk.Button(root, bg="black", height=1, width=7, command=d)
sa5c.grid(row = 2, column = 5)

sa6c = tk.Button(root, bg="black", height=1, width=7, command=eb)
sa6c.grid(row = 2, column = 6)

sa7c = tk.Button(root, bg="black", height=1, width=7, command=e1)
sa7c.grid(row = 2, column = 7)

sa8c = tk.Button(root, bg="black", height=1, width=7, command=f1)
sa8c.grid(row = 2, column = 8)

sa9c = tk.Button(root, bg="black", height=1, width=7, command=gb1)
sa9c.grid(row = 2, column = 9)

sa10c = tk.Button(root, bg="black", height=1, width=7, command=g1)
sa10c.grid(row = 2, column = 10)

sa11c = tk.Button(root, bg="black", height=1, width=7, command=ab1)
sa11c.grid(row = 2, column = 11)

sa12c = tk.Button(root, bg="black", height=1, width=7, command=a1)
sa12c.grid(row = 2, column = 12)

sa13c = tk.Button(root, bg="black", height=1, width=7, command=bb1)
sa13c.grid(row = 2, column = 13)

sa14c = tk.Button(root, bg="black", height=1, width=7, command=b1)
sa14c.grid(row = 2, column = 14)

sa15c = tk.Button(root, bg="black", height=1, width=7, command=c1)
sa15c.grid(row = 2, column = 15)

sa16c = tk.Button(root, bg="black", height=1, width=7, command=db1)
sa16c.grid(row = 2, column = 16)

sa17c = tk.Button(root, bg="black", height=1, width=7, command=d1)
sa17c.grid(row = 2, column = 17)

sa18c = tk.Button(root, bg="black", height=1, width=7, command=eb1)
sa18c.grid(row = 2, column = 18)



sdc = tk.Button(root, bg="black", height=1, width=7, command=d)
sdc.grid(row = 1, column = 0)

sd1c = tk.Button(root, bg="black", height=1, width=7, command=eb)
sd1c.grid(row = 1, column = 1)

sd2c = tk.Button(root, bg="black", height=1, width=7, command=e1)
sd2c.grid(row = 1, column = 2)

sd3c = tk.Button(root, bg="black", height=1, width=7, command=f1)
sd3c.grid(row = 1, column = 3)

sd4c = tk.Button(root, bg="black", height=1, width=7, command=gb1)
sd4c.grid(row = 1, column = 4)

sd5c = tk.Button(root, bg="black", height=1, width=7, command=g1)
sd5c.grid(row = 1, column = 5)

sd6c = tk.Button(root, bg="black", height=1, width=7, command=ab1)
sd6c.grid(row = 1, column = 6)

sd7c = tk.Button(root, bg="black", height=1, width=7, command=a1)
sd7c.grid(row = 1, column = 7)

sd8c = tk.Button(root, bg="black", height=1, width=7, command=bb1)
sd8c.grid(row = 1, column = 8)

sd9c = tk.Button(root, bg="black", height=1, width=7, command=b1)
sd9c.grid(row = 1, column = 9)

sd10c = tk.Button(root, bg="black", height=1, width=7, command=c1)
sd10c.grid(row = 1, column = 10)

sd11c = tk.Button(root, bg="black", height=1, width=7, command=db1)
sd11c.grid(row = 1, column = 11)

sd12c = tk.Button(root, bg="black", height=1, width=7, command=d1)
sd12c.grid(row = 1, column = 12)

sd13c = tk.Button(root, bg="black", height=1, width=7, command=eb1)
sd13c.grid(row = 1, column = 13)

sd14c = tk.Button(root, bg="black", height=1, width=7, command=e2)
sd14c.grid(row = 1, column = 14)

sd15c = tk.Button(root, bg="black", height=1, width=7, command=f2)
sd15c.grid(row = 1, column = 15)

sd16c = tk.Button(root, bg="black", height=1, width=7, command=gb2)
sd16c.grid(row = 1, column = 16)

sd17c = tk.Button(root, bg="black", height=1, width=7, command=g2)
sd17c.grid(row = 1, column = 17)

sd18c = tk.Button(root, bg="black", height=1, width=7, command=ab2)
sd18c.grid(row = 1, column = 18)



sgc = tk.Button(root, bg="black", height=1, width=7, command=g1)
sgc.grid(row = 0, column = 0)

sg1c = tk.Button(root, bg="black", height=1, width=7, command=ab1)
sg1c.grid(row = 0, column = 1)

sg2c = tk.Button(root, bg="black", height=1, width=7, command=a1)
sg2c.grid(row = 0, column = 2)

sg3c = tk.Button(root, bg="black", height=1, width=7, command=bb1)
sg3c.grid(row = 0, column = 3)

sg4c = tk.Button(root, bg="black", height=1, width=7, command=b1)
sg4c.grid(row = 0, column = 4)

sg5c = tk.Button(root, bg="black", height=1, width=7, command=c1)
sg5c.grid(row = 0, column = 5)

sg6c = tk.Button(root, bg="black", height=1, width=7, command=db1)
sg6c.grid(row = 0, column = 6)

sg7c = tk.Button(root, bg="black", height=1, width=7, command=d1)
sg7c.grid(row = 0, column = 7)

sg8c = tk.Button(root, bg="black", height=1, width=7, command=eb1)
sg8c.grid(row = 0, column = 8)

sg9c = tk.Button(root, bg="black", height=1, width=7, command=e2)
sg9c.grid(row = 0, column = 9)

sg10c = tk.Button(root, bg="black", height=1, width=7, command=f2)
sg10c.grid(row = 0, column = 10)

sg11c = tk.Button(root, bg="black", height=1, width=7, command=gb2)
sg11c.grid(row = 0, column = 11)

sg12c = tk.Button(root, bg="black", height=1, width=7, command=g2)
sg12c.grid(row = 0, column = 12)

sg13c = tk.Button(root, bg="black", height=1, width=7, command=ab2)
sg13c.grid(row = 0, column = 13)

sg14c = tk.Button(root, bg="black", height=1, width=7, command=a2)
sg14c.grid(row = 0, column = 14)

sg15c = tk.Button(root, bg="black", height=1, width=7, command=bb2)
sg15c.grid(row = 0, column = 15)

sg16c = tk.Button(root, bg="black", height=1, width=7, command=b2)
sg16c.grid(row = 0, column = 16)

sg17c = tk.Button(root, bg="black", height=1, width=7, command=c2)
sg17c.grid(row = 0, column = 17)

sg18c = tk.Button(root, bg="black", height=1, width=7, command=db2)
sg18c.grid(row = 0, column = 18)



root.mainloop() #repeats infinetly