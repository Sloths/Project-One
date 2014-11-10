from Tkinter import *
import ttk
import random
import time
import Tkinter as tk
import ctypes

#Creating window and canvas
window = Tk()
canvas = Canvas(window, width=854, height=480, bg='white')
canvas.pack()
window.title('Sloths Virtual Robot')
window.geometry('{}x{}'. format(874,568))
window.resizable(width=FALSE, height=FALSE)

#countdown is set to 61 seconds
countdown = 61

#loading images
gif1 = PhotoImage(file="image1.gif")
gif2 = PhotoImage(file="image2.gif")
gif3 = PhotoImage(file="image3.gif")
gif4 = PhotoImage(file="image4.gif")

#Stop Function defined as Global 
def Stop():
    global programRunning
    programRunning = False
    #stopping timer   
    global countdown
    countdown = 1
    #Deleting robot    
    global rb1
    canvas.delete(rb1)
    #Enables buttons so user can change map once game has stopped
    btnMap1.config(state='normal')
    btnMap2.config(state='normal')
    btnMap3.config(state='normal')
    btnMap4.config(state='normal')
    
#Start Function
def Start():
    # create screen boundaries
    x_min = 0.0
    y_min = 0.0
    x_max = 854.0
    y_max = 480.0

    # set movement velocity
    vx = 10.0 # x velocity
    vy = 5.0 # y velocity

    # Random Respawn of Robot
    # random x coordinate selected from the range
    rbx = random.randrange(0, 854, 1)
    # random y coordinate selected from the range
    rby = random.randrange(0,480, 1)
    global rb1
    # creation of the robot
    rb1 = canvas.create_rectangle(rbx, rby, rbx + 10, rby + 10, fill = "blue", outline='blue')
    
    #Generate Map 1
    global ob1
    ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green', width=3)
    global ob2
    ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green', width=3)
    global ob3
    ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green', width=3)
    global ob4
    ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green', width=3)
    global ob5
    ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green', width=3)

    #Disables map buttons so user cannot change map while running
    btnMap1.config(state='disabled')
    btnMap2.config(state='disabled')
    btnMap3.config(state='disabled')
    btnMap4.config(state='disabled')

    #Countdown function
    def counter_label(label):
      global countdown
      countdown = 61
      def count():
        global countdown
        global programRunning
        #Decrease countdown by 1
        countdown -= 1
        if countdown <= 0:
          programRunning = False
          label.config(text=str(countdown))
          #Enables buttons so user can change map once game has stopped
          btnMap1.config(state='normal')
          btnMap2.config(state='normal')
          btnMap3.config(state='normal')
          btnMap4.config(state='normal')
          #Message box to user
          ctypes.windll.user32.MessageBoxA(0, "The timer has run out!", "Time up!", 0)
        elif countdown > 0:
          programRunning = True
          label.config(text=str(countdown))
          #after a thousand ticks call count function 
          label.after(1000, count)
          #random colour change of objects every 5 seconds
        if countdown % 5 == 0:
          # randomly select an object to turn red in the range
          red = random.randrange(1,5,1)
          if red == 1:
            ob1=canvas.create_rectangle(100, 100, 200, 170,fill='red',outline='red',width=3)
            ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green',outline='green',width=3)
            ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green',outline='green',width=3)
            ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green',outline='green',width=3)
            ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green',outline='green',width=3)
          elif red ==2:
            ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green',outline='green',width=3)
            ob2=canvas.create_rectangle(754, 100, 654, 170,fill='red',outline='red',width=3)
            ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green',outline='green',width=3)
            ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green',outline='green',width=3)
            ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green',outline='green',width=3)
          elif red ==3:
            ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green',outline='green',width=3)
            ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green',outline='green',width=3)
            ob3=canvas.create_rectangle(550, 280, 300, 200,fill='red',outline='red',width=3)
            ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green',outline='green',width=3)
            ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green',outline='green',width=3)
          elif red==4:
            ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green',outline='green', width=3)
            ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green',outline='green', width=3)
            ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green',outline='green', width=3)
            ob4=canvas.create_rectangle(100, 380, 200, 310,fill='red',outline='red', width=3)
            ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green',outline='green', width=3)
          elif red==5:
            ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green',outline='green', width=3)
            ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green',outline='green', width=3)
            ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green',outline='green', width=3)
            ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green',outline='green', width=3)
            ob5=canvas.create_rectangle(754, 380, 654, 310,fill='red',outline='red', width=3)
      count()
    counter_label(label)
   

    #Define as a global variable once to keep using
    global programRunning
    programRunning = True

    while programRunning == True:  

        # create shape coordinates        
        rx1, ry1, rx2, ry2 = canvas.coords(rb1)

        # robot boundary detection and response
        if rx1 <= x_min + 10:
            vx = 10.0
        if ry1 <= y_min + 10:
            vy = 5.0
        if rx2 >= x_max - 10:
            vx = -10.0
        if ry2 >= y_max - 10:
            vy = -5.0        
        
        global red
             
        objList = [ob1, ob2, ob3, ob4, ob5]
        
        for o in objList:
            x1, y1, x2, y2 = canvas.coords(o)
            
            if rx1 > (x2 - 10) and rx1 < (x2 + 10) and ry1 > y1 and ry1 < y2: # right side of object
                if vy == 5.0 and vx == -10.0:
                    vy = 5.0
                    vx = 10.0                   
                if vy == -5.0 and vx == -10.0:
                    vy = -5.0
                    vx = 10.0                    
            
            if rx2 < (x1 + 10) and rx2 > (x1 - 10) and ry1 > y1 and ry2 < y2: # left side of object
                if vy == 5.0 and vx == 10.0:
                    vy = 5.0
                    vx = -10.0                    
                if vy == -5.0 and vx == -10.0:
                    vy = -5.0
                    vx = 10.0                    
            
            if ry2 > (y1 - 10) and ry2 < (y1 + 10) and rx1 > x1 and rx1 < x2: # top side of object
                if vy == 5.0 and vx == 10.0:
                    vy = -5.0
                    vx = 10.0                    
                if vy == 5.0 and vx == -10.0:
                    vy = -5.0
                    vx = -10.0
                                    
            if ry1 < (y2 + 10) and ry1 > (y2 - 10) and rx1 > x1 and rx1 < x2: # bottom side of object
                if vx == 10.0 and vy == -5.0:
                    vy = 5.0
                    vx = 10.0                    
                if vy == -5.0 and vx == -10.0:
                    vy = 5.0
                    vx = -10.0        
        
        # reposition moving objects
        canvas.coords(rb1, rx1 + vx, ry1 + vy, rx2 + vx, ry2 + vy)
        canvas.update()

        # Sleep for 0.1 seconds, then delete the image.
        time.sleep(0.1)      

#Reset Function
def Reset():
    canvas.delete("img") 

#Map 1 Function
def Map1():
    canvas.delete("all")
    ob1=canvas.create_rectangle(100, 100, 200, 170,fill='white', width=3)
    ob2=canvas.create_rectangle(754, 100, 654, 170,fill='white', width=3)
    ob3=canvas.create_rectangle(550, 280, 300, 200,fill='white', width=3)
    ob4=canvas.create_rectangle(100, 380, 200, 310,fill='white', width=3)
    ob5=canvas.create_rectangle(754, 380, 654, 310,fill='white', width=3)

#Loading image functions
def Image1():
    global gif1
    image1=canvas.create_image(0,0,image=gif1,anchor="nw",tag="img")
def Image2():
    global gif2
    image2=canvas.create_image(0,0,image=gif2,anchor="nw",tag="img")
def Image3():
    global gif3
    image3=canvas.create_image(0,0,image=gif3,anchor="nw",tag="img")
def Image4():
    global gif4
    image4=canvas.create_image(0,0,image=gif4,anchor="nw",tag="img")
                               
#Creating buttons
btnStart=Button(window, text='Start', height=1, width=20, command=Start)
btnStop=Button(window, text='Stop', height=1, width=20, command=Stop)
btnReset=Button(window, text='Reset', height=1, width=20, command=Reset)

#Places buttons in correct positions
btnStart.place(x=11, y=500)
btnStop.place(x=11, y=530)
btnReset.place(x=712, y=530)

#Creating countdown label
label= tk.Label(font=('Helvetica', 20))
label.place(x=400, y=500)
label.pack()

#Creating image buttons
btnMap1=Button(window, text="1", height=1, width=2, command=Image1)
btnMap2=Button(window, text="2", height=1, width=2, command=Image2)
btnMap3=Button(window, text="3", height=1, width=2, command=Image3)
btnMap4=Button(window, text="4", height=1, width=2, command=Image4)

#Placement of image buttons
btnMap1.place(x=712, y=500)
btnMap2.place(x=754, y=500)
btnMap3.place(x=797, y=500)
btnMap4.place(x=837, y=500)

#Padds canvas
canvas.pack(padx=10,pady=10)

window.mainloop()
