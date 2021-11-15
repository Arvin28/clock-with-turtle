
from tkinter import *
import time
from typing import Sized
win = Tk()
win.geometry('400x300')
win.config(bg='blue')

sec = IntVar()
Entry(win, textvariable=sec, width = 2,).place(x=220, y=120)
sec.set('00')
mins= IntVar()
Entry(win, textvariable = mins, width =2,).place (x=180, y=120) 

mins.set('00')
hrs= IntVar()
Entry(win, textvariable = hrs, width =2,).place(x=142, y=120)
hrs.set('00')

def countdowntimer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      
      win.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1
Label(win,font="Times 20 italic bold", text = 'Timer',bg='blue',bd=5).place(x=150,y=70)

Button(win, text='START', bd ='5', bg= ("green"),command = countdowntimer,width=15,height=4).place(x=135, y=165)

Button(win,text="Stop",width=5,height=2).place (x=50,y=100)







win.mainloop()