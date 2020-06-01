import tkinter as tk #imports tkinter

txt="" #starts top text as empty
messagesinbox=["What colour do you want","What text colour do you want"] #shows what the player is changing
message=messagesinbox[0] #shows which message is showing
colour="white" #shows background colour
textcolour="black" #shows text colour
count=0 #shows a capitalised counter
messagecount=0 #shows which message is showing

letters=[["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"],["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]]
#shows the letters





root=tk.Tk() #start tk loop
class key: #class for buttons
    def __init__(self,rowe,columne,text,com):
        if count%2==0: #if change is not capitalised
            self.text=text #changes text to be lowercase
        else: #if change is capitalised
            self.text=text.upper() #changes text to be uppercase
        self.rower=rowe
        self.columner=columne
        self.colour=colour
        self.txtcol=textcolour
        self=tk.Button(root, height=1,width=2,fg=self.txtcol,bg=self.colour,text=self.text, command=com)
        self.grid(row=rowe,column=columne)


class doublecolumn:
    def __init__(self,rowe,columne,text,com):
        self.text=text
        self.rower=rowe
        self.columner=columne
        self.colour=colour
        self.txtcol = textcolour
        if com==0:
            self = tk.Button(root, height=2,fg=self.txtcol, width=2,bg=self.colour, text=self.text)
        else:
            self=tk.Button(root,height=2,fg=self.txtcol,width=2,bg=self.colour, text=self.text,command=com)
        self.grid(row=rowe,column=columne, rowspan=2)


class textkey:
    def __init__(self,rowe,columne,text,com):
        self.text=text
        self.rower=rowe
        self.columner=columne
        self.colour=colour
        self.txtcol = textcolour
        if com==0:
            self = tk.Button(root,fg=self.txtcol, height=1, width=30,bg=self.colour, text=self.text)
        else:
            self=tk.Button(root,fg=self.txtcol,height=1,width=30,bg=self.colour, text=self.text,command=com)
        self.grid(row=rowe,column=columne, columnspan=250)

class fin:
    def __init__(self,rowe,columne,text,com):
        self.text=text
        self.rower=rowe
        self.columner=columne
        self.colour=colour
        self.txtcol = textcolour
        if com==0:
            self = tk.Button(root,fg=self.txtcol, height=1, width=5,bg=self.colour, text=self.text)
        else:
            self=tk.Button(root,fg=self.txtcol,height=1,width=5, text=self.text,bg=self.colour,command=com)
        self.grid(row=rowe,column=columne, columnspan=2)



#function for is button 1 is pressed
def one():
    global enter,txt
    txt=txt+"1" #adds 1 to message
    enter=textkey(1,0,txt,0) #changes message depending
#repeat for all buttons

def two():
    global enter,txt
    txt=txt+"2"
    enter=textkey(1,0,txt,0)

def three():
    global enter,txt
    txt=txt+"3"
    enter=textkey(1,0,txt,0)

def four():
    global enter,txt
    txt=txt+"4"
    enter=textkey(1,0,txt,0)

def five():
    global enter,txt
    txt=txt+"5"
    enter=textkey(1,0,txt,0)

def six():
    global enter,txt
    txt=txt+"6"
    enter=textkey(1,0,txt,0)

def seven():
    global enter,txt
    txt=txt+"7"
    enter=textkey(1,0,txt,0)

def eight():
    global enter,txt
    txt=txt+"8"
    enter=textkey(1,0,txt,0)

def nine():
    global enter,txt
    txt=txt+"9"
    enter=textkey(1,0,txt,0)

def zero():
    global enter,txt
    txt=txt+"0"
    enter=textkey(1,0,txt,0)



def q():
    global enter,txt
    txt=txt+letters[count%2][0]
    enter=textkey(1,0,txt,0)

def w():
    global enter,txt
    txt=txt+letters[count%2][1]
    enter=textkey(1,0,txt,0)

def e():
    global enter,txt
    txt=txt+letters[count%2][2]
    enter=textkey(1,0,txt,0)

def r():
    global enter,txt
    txt=txt+letters[count%2][3]
    enter=textkey(1,0,txt,0)

def t():
    global enter,txt
    txt=txt+letters[count%2][4]
    enter=textkey(1,0,txt,0)

def y():
    global enter,txt
    txt=txt+letters[count%2][5]
    enter=textkey(1,0,txt,0)

def u():
    global enter,txt
    txt=txt+letters[count%2][6]
    enter=textkey(1,0,txt,0)

def i():
    global enter,txt
    txt=txt+letters[count%2][7]
    enter=textkey(1,0,txt,0)

def o():
    global enter,txt
    txt=txt+letters[count%2][8]
    enter=textkey(1,0,txt,0)

def p():
    global enter,txt
    txt=txt+letters[count%2][9]
    enter=textkey(1,0,txt,0)


def a():
    global enter, txt
    txt = txt + letters[count%2][10]
    enter = textkey(1, 0, txt,0)


def s():
    global enter, txt
    txt = txt + letters[count%2][11]
    enter = textkey(1, 0, txt,0)


def d():
    global enter, txt
    txt = txt + letters[count%2][12]
    enter = textkey(1, 0, txt,0)


def f():
    global enter, txt
    txt = txt + letters[count%2][13]
    enter = textkey(1, 0, txt,0)


def g():
    global enter, txt
    txt = txt + letters[count%2][14]
    enter = textkey(1, 0, txt,0)


def h():
    global enter, txt
    txt = txt + letters[count%2][15]
    enter = textkey(1, 0, txt,0)


def j():
    global enter, txt
    txt = txt + letters[count%2][16]
    enter = textkey(1, 0, txt,0)


def k():
    global enter, txt
    txt = txt + letters[count%2][17]
    enter = textkey(1, 0, txt,0)


def l():
    global enter, txt
    txt = txt + letters[count%2][18]
    enter = textkey(1, 0, txt,0)


def z():
    global enter, txt
    txt = txt + letters[count%2][19]
    enter = textkey(1, 0, txt,0)


def x():
    global enter, txt
    txt = txt + letters[count%2][20]
    enter = textkey(1, 0, txt,0)


def c():
    global enter, txt
    txt = txt + letters[count%2][21]
    enter = textkey(1, 0, txt,0)


def v():
    global enter, txt
    txt = txt + letters[count%2][22]
    enter = textkey(1, 0, txt,0)


def b():
    global enter, txt
    txt = txt + letters[count%2][23]
    enter = textkey(1, 0, txt,0)


def n():
    global enter, txt
    txt = txt + letters[count%2][24]
    enter = textkey(1, 0, txt,0)


def m():
    global enter, txt
    txt = txt + letters[count%2][25]
    enter = textkey(1, 0, txt,0)

def swap():
    global messages,messagecount,message,comment
    messagecount=messagecount+1
    message=messagesinbox[messagecount%2]
    comment = textkey(0, 0, message, 0)

def spacebar():
    global enter, txt
    txt = txt + " "
    enter = textkey(1, 0, txt,0)

def backspace():
    global enter, txt
    length=len(txt)
    length=length-1
    parta=txt[0:length]
    partb=""
    txt=parta+partb
    enter = textkey(1, 0, txt,0)

def hashkey():
    global enter, txt
    txt = txt + "#"
    enter = textkey(1, 0, txt,0)

def capslock(): #changes all buttons to be capitalised
    global count,letts
    count=count+1
    letts=[key(4,0,"q",q),key(4,1,"w",w),key(4,2,"e",e),key(4,3,"r",r),key(4,4,"t",t),key(4,5,"y",y),key(4,6,"u",u),key(4,7,"i",i),key(4,8,"o",o),key(4,9,"p",p),key(5,0,"a",a),key(5,1,"s",s),key(5,2,"d",d),key(5,3,"f",f),key(5,4,"g",g),key(5,5,"h",h),key(5,6,"j",j),key(5,7,"k",k),key(5,8,"l",l),key(5,9,"#",hashkey),doublecolumn(5,10,"^",capslock),key(6,1,"z",z),key(6,2,"x",x),key(6,3,"c",c),key(6,4,"v",v),key(6,5,"b",b),key(6,6,"n",n),key(6,7,"m",m)]




def finish(): #completes the program
    global txt,message,colourchange,textcolour,letts,colour,enter,space,back,done,comment,nums
    origincolour=colour
    origintext=textcolour
    try:
        if messagecount%2==0:
            letts[0].colour=txt
            colour=txt


        else:
            letts[0].textcolour=txt
            textcolour=txt



        message=messagesinbox[messagecount%2]


        letts=[key(4,0,"q",q),key(4,1,"w",w),key(4,2,"e",e),key(4,3,"r",r),key(4,4,"t",t),key(4,5,"y",y),key(4,6,"u",u),key(4,7,"i",i),key(4,8,"o",o),key(4,9,"p",p),key(5,0,"a",a),key(5,1,"s",s),key(5,2,"d",d),key(5,3,"f",f),key(5,4,"g",g),key(5,5,"h",h),key(5,6,"j",j),key(5,7,"k",k),key(5,8,"l",l),key(5,9,"#",hashkey),doublecolumn(5,10,"^",capslock),key(6,1,"z",z),key(6,2,"x",x),key(6,3,"c",c),key(6,4,"v",v),key(6,5,"b",b),key(6,6,"n",n),key(6,7,"m",m)]
        nums=[key(3,0,"1",one),key(3,1,"2",two),key(3,2,"3",three),key(3,3,"4",four),key(3,4,"5",five),key(3,5,"6",six),key(3,6,"7",seven),key(3,7,"8",eight),key(3,8,"9",nine),key(3,9,"0",zero)]
        txt=""
        enter = textkey(1, 0, txt, 0)
        space = textkey(7, 0, "Space", spacebar)
        comment=textkey(0,0,message,0)
        back=key(6,0,"<",backspace)
        done=fin(6,8,"Done",finish)
        colourchange = key(3, 10, "=", swap)

#checks if the input is a valid number
    except tk.TclError:
        message="That is not a valid colour"
        colour=origincolour
        textcolour=origintext
        txt=""
        comment = textkey(0, 0, message, 0)
        txt=""
        enter = textkey(1, 0, txt, 0)

enter=textkey(1,0,"",0)
comment=textkey(0,0,message,0)
letts=[key(4,0,"q",q),key(4,1,"w",w),key(4,2,"e",e),key(4,3,"r",r),key(4,4,"t",t),key(4,5,"y",y),key(4,6,"u",u),key(4,7,"i",i),key(4,8,"o",o),key(4,9,"p",p),key(5,0,"a",a),key(5,1,"s",s),key(5,2,"d",d),key(5,3,"f",f),key(5,4,"g",g),key(5,5,"h",h),key(5,6,"j",j),key(5,7,"k",k),key(5,8,"l",l),key(5,9,"#",hashkey),doublecolumn(5,10,"^",capslock),key(6,1,"z",z),key(6,2,"x",x),key(6,3,"c",c),key(6,4,"v",v),key(6,5,"b",b),key(6,6,"n",n),key(6,7,"m",m)]
nums=[key(3,0,"1",one),key(3,1,"2",two),key(3,2,"3",three),key(3,3,"4",four),key(3,4,"5",five),key(3,5,"6",six),key(3,6,"7",seven),key(3,7,"8",eight),key(3,8,"9",nine),key(3,9,"0",zero)]
space=textkey(7,0,"Space",spacebar)
back=key(6,0,"<",backspace)
done=fin(6,8,"Done",finish)
colourchange=key(3,10,"=",swap)

root.mainloop()
