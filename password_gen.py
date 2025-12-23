from tkinter import *
import random
import string

root=Tk()
root.title("Password generator")
root.geometry("500x300")
root.resizable(False,False)


def password_generator():
    
     password=[]

     for i in range(4):

         lower=random.choice(string.ascii_lowercase)
         upper=random.choice(string.ascii_uppercase) 

         password.append(lower)
         password.append(upper)

     t="".join(password) 
     label.config(text=t)
    

        
label= Label(root,font=("times",40,"bold"))
label.pack()

Button(root,text="Generate",font=("Times",25,"bold"),command= password_generator).place(x=150,y=170)

Button(root,text="Exit",font=("Times",20,"bold"),command=quit).place(x=425,y=243)

root.mainloop()


