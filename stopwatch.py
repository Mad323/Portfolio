from pickletools import markobject
from sre_constants import MARK
from tkinter import *
from datetime import datetime

root=Tk()
root.title("stopwatch")
root.geometry("900x400+400+100")
root.minsize(200,300)
root.maxsize(1400,1600)
run =False
count=18000    

def fun_0(mark):
  def value():
 		if run==True:
 			global count  
 			if count==18000:
 				show="Starting"
 			else:
 				tt = datetime.fromtimestamp(count)  #  
 				show = tt.strftime("%H:%M:%S")   #  
 			mark['text']=show
			

 			mark.after(1000,value)
			count=count+1 
 	value()


def fun_1(mark):
 	global run
 	run = True
 	fun_0(mark)
 	start['state'] = 'disabled' ; stop['state'] = 'normal' ; reset['state'] = 'normal'
	

def fun_2():
 	global run
 	start['state']= 'normal'; stop['state']= 'disabled'; reset['state']= 'normal'
 	run=False

def fun_3(mark):
 	global count
 	count=18000
 	if run==False:   # stop   >>  welcome 
 		reset['state']='disabled'; mark['text']='Welcome'
 	else:
 		mark['text']='Starting'





mark = Label(root,text="Welcome",fg="blue",font=("Times New Roman",20,"bold"),bg="pink")mark.place(x=45,y=45)

start= Button(root,text="Start", bg="red",fg="orange",command=lambda:fun_1(mark), font=("Times New Roman",20,"bold"))
start.place(x=115,y=200)

stop =Button(root,text="Stop",bg="blue",fg="pink",state="disabled",command=fun_2,font=("Times New Roman",20,"bold"))
stop.place(x=200,y=200)

reset=Button(root,text="Reset",bg="pink",fg="orange",state="disabled", command=lambda:fun_3(mark),font=("Times New Roman",20,"bold"))
reset.place(x=300,y=200)


root.mainloop()
