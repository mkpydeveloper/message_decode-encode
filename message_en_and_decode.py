from tkinter import *
import base64

# step 1 :- intilize window
import enc as enc

root = Tk()  #intilized tkinter which means windows created
root.geometry('500x300') # set the width and height of the windows
root.resizable(0,0)# set the fixed size of windows
root.title("whypython - message encode and decode ")

Label(root ,text =' Encode Decode ' , font = ' arial 20 bold ').pack()

Label(root ,text =' whypython ' , font = 'arial 20 bold ').pack(side = BOTTOM)

#Label()  widget use to display one or more than one lines of text that user aren't change
#it

#root = is the name which we use to  refer to our window
#text = which we display on the label
#font = in which the text is written
#pack = orginized the widget block

# step 2 :- define variable
Text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

# Text = variable store the message to encode and decode
# private_key = variable store to private key to use to encode and decode
# mode = is used to select that is either encoding and decoding
#result = store the result

#step 3 :- function of encode

def encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#step 4 :- function of decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)
# step 6:- function to set mode

def Mode():
    if(mode.get() == 'e' ):
        result.set(encode(private_key.get(),Text.get()))
    elif(mode.get()  == 'd'):
        result.set(Decode(private_key.get(),Text.get()))
    else :
        result.set('invalid mode')

# step 7:- exit window

def Exit():
    root.destroy()

# step 8:- function to reset the window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    result.set("")

Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()