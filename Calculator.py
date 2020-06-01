import tkinter as tk,random,time

sum=[] #holds the parts of the calculation
calculation=[] #holds the numbers of the calculation
message="" #holds the text for the calculator
currentnum=0 #holds currentnumber
complete=0 #sees if the calculation is complete


nums=["0","1","2","3","4","5","6","7","8","9","+","-","x","÷","^"] #holds the text for the buttons

function=["+","-","x","÷","^"] #holds the buttons with functions
root=tk.Tk() #starts tkinter



class numbers: #class for number buttons
    def __init__(self,rowa,columna,text,com):
        self.text=text
        self=tk.Button(root, height=1,width=2,text=text, command=com)
        self.grid(row=rowa,column=columna)

class equal: #class for function buttons
    def __init__(self,rowa,columna,text,com):
        self.text=text
        self=tk.Button(root, height=1,width=5,text=self.text,command=com)
        self.grid(row=rowa,column=columna, columnspan=2)

class textkey: #class for bars
    def __init__(self,rowa,columna,text,com):
        self=tk.Button(root,height=1,width=30, text=text,command=com)
        self.grid(row=rowa,column=columna, columnspan=250)

def cero(): #function for 0
    global message,comment,complete
    if complete==1: #if solved
        message="" #resets message
        complete=0 #shows not completed
    message=message+nums[0] #changes the message
    comment=textkey(0,0,message,0) #changes message in button
    sum.append(nums[0]) #changes the text in the array
#repeat for all numbers

def uno():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[1]
    comment=textkey(0,0,message,0)
    sum.append(nums[1])

def dos():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[2]
    comment=textkey(0,0,message,0)
    sum.append(nums[2])

def tres():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[3]
    comment=textkey(0,0,message,0)
    sum.append(nums[3])

def cuatro():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[4]
    comment=textkey(0,0,message,0)
    sum.append(nums[4])

def cinco():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[5]
    comment=textkey(0,0,message,0)
    sum.append(nums[5])

def seis():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[6]
    comment=textkey(0,0,message,0)
    sum.append(nums[6])

def siete():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[7]
    comment=textkey(0,0,message,0)
    sum.append(nums[7])

def ocho():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[8]
    comment=textkey(0,0,message,0)
    sum.append(nums[8])

def nueve():
    global message,comment,complete
    if complete==1:
        message=""
        complete=0
    message=message+nums[9]
    comment=textkey(0,0,message,0)
    sum.append(nums[9])

def answ(): #function for the answer button
    global value,message,comment,complete
    message=value #changes the message
    comment=textkey(0,0,message,0) #changes message in button
    sum.append(value) #adds to the array for the calculation
    complete=0 #resets complete to 0

def add(): #function for add button
    global message,comment,complete
    if complete == 1: #if solved
        message = value #new message is +
        sum.append(value) #array for calc becomes +
    message=message+nums[10] #changes the message so it has +
    comment=textkey(0,0,message,0) #changes message in button
    sum.append(nums[10]) #array for calc appended +
    complete = 0 #sets complete to 0
#repeat for all function buttons

def subtract():
    global message,comment,complete
    if complete == 1:
        message = value
        sum.append(value)
    message=message+nums[11]
    comment=textkey(0,0,message,0)
    sum.append(nums[11])
    complete = 0

def multiply():
    global message,comment,complete
    if complete == 1:
        message = value
        sum.append(value)
    message=message+nums[12]
    comment=textkey(0,0,message,0)
    sum.append(nums[12])
    complete = 0

def divide():
    global message,comment,complete
    if complete == 1:
        message = value
        sum.append(value)
    message=message+nums[13]
    comment=textkey(0,0,message,0)
    sum.append(nums[13])
    complete = 0

def powerof():
    global message,comment,complete
    if complete == 1:
        message = value
        sum.append(value)
    message=message+nums[14]
    comment=textkey(0,0,message,0)
    sum.append(nums[14])
    complete = 0



def backspace(): #removes last character
    global comment,message
    length=len(message) #finds length of message
    length=length-1 #decreases length by 1
    parta=message[0:length] #takes the first part of the message
    partb=""
    message=parta+partb #changes the message
    comment=textkey(0,0,message,0) #changes message in button
    sum.pop(len(sum)-1) #removes last character of array holding character

def result():
    global currentnum,message,comment,complete,sum,value,brackets,inbracks
    currentnum=0 #changes the currentnumber to 0
    calculation=[] #empties the calculation
    count=1 #sets the counter to see what power of 10 is in use
    power=0 #sets a power to 0
    sum.append("+") #adds a + to the end of the array
    for i in range(0, len(sum)):
        if sum[i] not in function or sum[i]=="^": #sees if the character is a function number
            if sum[i] == "^": #checks if the character is a power
                held=currentnum #shows the held number
                count=1 #resets the counter to 1
                power=1 #sets a power to 1
                currentnum = 0

            else:
                currentnum=(currentnum/(count/10))*count+int(sum[i]) #if multiple digits in number
                count=count*10 #increases the counter
        else:
            count=1 #resets count


            if power==1: #if there is a power
                held=held**currentnum #finds the power of a the number
                currentnum=held #changes the currentnum to held
                calculation.append(currentnum) #adds all numbers into 1 index rather than seperate indexes

            else:
                calculation.append(currentnum) #adds numbers to calc
                calculation.append(sum[i]) #adds the index position of the calc
            currentnum=0
    #print(calculation)
    calculation.append(currentnum)
    value=calculation[0]
    for i in range(2,len(calculation),2): #runs through the calculation
        if calculation[i-1]=="+": #if the current index - 1 holds +
                value=value+calculation[i] #adds the current index to the total value
        #same as above but for different functions
        elif calculation[i-1]=="-":
                value=value-calculation[i]
        elif calculation[i-1]=="x":
                value=value*calculation[i]
        elif calculation[i - 1] == "÷":
                value=value/calculation[i]


    message=str(int(value)) #changes the message to the total value
    value=str(message) #changes the value for the string of the message
    comment=textkey(0,0,message,0) #changes message in button
    complete=1 #changes complete to 1
    sum=[] #sets sum to no index


comment=textkey(0,0,message,0) #sets all buttons
one=numbers(50,0,"1",uno)
two=numbers(50,1,"2",dos)
three=numbers(50,2,"3",tres)
four=numbers(51,0,"4",cuatro)
five=numbers(51,1,"5",cinco)
six=numbers(51,2,"6",seis)
seven=numbers(52,0,"7",siete)
eight=numbers(52,1,"8",ocho)
nine=numbers(52,2,"9",nueve)
zero=numbers(53,0,"0",cero)
answer=equal(53,1,"=",result)

plus=numbers(51,4,"+",add)
sub=numbers(51,5,"-",subtract)
times=numbers(52,4,"x",multiply)
div=numbers(52,5,"÷",divide)
ans=equal(53,4,"ANS",answ)
back=numbers(53,6,"<",backspace)
power=numbers(50,4,"^",powerof)

root.mainloop()
