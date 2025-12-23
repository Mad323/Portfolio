import time
from tkinter import *
from tkinter import messagebox



root=Tk()
root.title("timer")
root.geometry("900x400+400+100")
root.minsize(200,300)
root.maxsize(1400,1600)

hour=StringVar(); minute=StringVar(); second=StringVar()
hour.set("00"); minute.set("00"); second.set("00")

hourEntry=Entry(root, width=3, font=("Arial",18,"" ), textvariable=hour).place(x=80,y=20)
minuteEntry=Entry(root, width=3, font=("Arial",18,"" ), textvariable=minute).place(x=130,y=20)
secondEntry=Entry(root, width=3, font=("Arial",18,"" ), textvariable=second).place(x=180,y=20)



def sumbit():
    
    try: #
        temp=int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:#
        print("Please input right value")
    
    while temp>-1:
        mins,secs=divmod(temp,60)

        hours=0#

        if mins>60:

            hours,mins= divmod(mins,60)#


        hour.set("{0:2d}".format(hours))#
        minute.set("{0:2d}".format(mins))#
        second.set("{0:2d}".format(secs))#
        root.update()
        time.sleep(1)
        if temp==0:
            messagebox.showinfo("Time Coundown", "Times up")

    temp-=1

Button(root,text="Set Time Countdown", command=sumbit,bd=5,relief=GROOVE).place(x=70,y=120)

root.mainloop()
