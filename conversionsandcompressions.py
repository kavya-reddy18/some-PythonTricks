import os
from tkinter import *
master = Tk()
master.title("Conversions and Compressions")
lis=[]
var1 = StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
def fun():
    inp=e1.get()
    outp=e2.get()
    a=var1.get()
    b=var2.get()
    c=var3.get()
    d=var4.get()
    e=var5.get()
    f=var6.get()
    g=var7.get()
    h=var8.get()
    if(a=='1'):
        lis.append("mp3")
    if(b=='1'):
        lis.append("mp2")
    if(c=='1'):
        lis.append("wav")
    if(d=='1'):
        lis.append("aac")
    if(e=='1'):
        lis.append("aiff")
    if(f=='1'):
        lis.append("asf")
    if(g=='1'):
        lis.append("flv")
    if(h=='1'):
        lis.append("caf")
    que="ffmpeg -i "+inp+"."+lis[0]+" "+outp+"."+lis[1]
    os.system(que)
    var1.set(None)
    var2.set(None)
    var3.set(None)
    var4.set(None)
    var5.set(None)
    var6.set(None)
    var7.set(None)
    var8.set(None)
    e1.set(None)
    e2.set(None)
    e3.set(None)
    Inp_name.set("")
    Output_name.set("")
def func():
    inp=e1.get()
    outp=e2.get()
    bi=e3.get()
    a=var1.get()
    b=var2.get()
    c=var3.get()
    d=var4.get()
    e=var5.get()
    f=var6.get()
    g=var7.get()
    h=var8.get()
    if(a=='1'):
        lis.append("mp3")
    if(b=='1'):
        lis.append("mp2")
    if(c=='1'):
        lis.append("wav")
    if(d=='1'):
        lis.append("aac")
    if(e=='1'):
        lis.append("aiff")
    if(f=='1'):
        lis.append("asf")
    if(g=='1'):
        lis.append("flv")
    if(h=='1'):
        lis.append("caf")
    que="ffmpeg -i "+inp+"."+lis[0]+" -b:a "+bi+"k "+outp+"."+lis[0]
    os.system(que)
    var1.set(None)
    var2.set(None)
    var3.set(None)
    var4.set(None)
    var5.set(None)
    var6.set(None)
    var7.set(None)
    var8.set(None) 
    Inp_name.set("")
    Output_name.set("")
Checkbutton(master,text='mp3',variable=var1).grid(row=0,sticky=W)
Checkbutton(master,text='mp2',variable=var2).grid(row=1,sticky=W)
Checkbutton(master,text='wav',variable=var3).grid(row=2,sticky=W)
Checkbutton(master,text='aac',variable=var4).grid(row=3,sticky=W)
Checkbutton(master,text='aiff',variable=var5).grid(row=4,sticky=W)
Checkbutton(master,text='asf',variable=var6).grid(row=5,sticky=W)
Checkbutton(master,text='flv',variable=var7).grid(row=6,sticky=W)
Checkbutton(master,text='caf',variable=var8).grid(row=7,sticky=W)
Label(master,text='input filename').grid(row=8)
Label(master,text='output filename').grid(row=9)
Label(master,text="bitrate").grid(row=10)
e1=Entry(master,text="Inp_name")
e2=Entry(master,text="Output_name")
e3=Entry(master,text="Bitrate")
e1.grid(row=8, column=1)
e2.grid(row=9, column=1)
e3.grid(row=10,column=1)
Button(master,text="convert",command=fun).grid(row=11,column=0)
Button(master,text="compress",command=func).grid(row=11,column=1)
mainloop()