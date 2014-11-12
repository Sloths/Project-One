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

#Number of games played to keep track
intPlay = 0

#Map button pressed intilised
ButtonPressed = 1

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
    global btnStopPressed
    btnStopPressed = True
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
    r1vx = 10.0 # x velocity for robot 1
    r1vy = 5.0 # y velocity for robot 1
    r2vx = -10.0 # x velocity for robot 2
    r2vy = -5.0 # velocity for robot 2

    global ButtonPressed
    if ButtonPressed == 1:
        MapLoad1()
    elif ButtonPressed == 2:
        MapLoad2()
    elif ButtonPressed == 3:
        MapLoad3()
    elif ButtonPressed == 4:
        MapLoad4()

    # Random Respawn of Robot
    # random x coordinate selected from the range
    rbx = random.randint(0, 844)
    # random y coordinate selected from the range
    rby = random.randint(0, 470)
    global rb1
    global rb2
    global intPlay
    #Deleting robot from last game
    if intPlay > 0:
        canvas.delete(rb1)
        canvas.delete(rb2)
        
    # creation of the robot
    rb1 = canvas.create_rectangle(rbx, rby, rbx + 10, rby + 10, fill = "cyan", outline = "blue")
    rb2 = canvas.create_rectangle(rbx, rby, rbx + 10, rby + 10, fill = "pink", outline = "deep pink")


    #Disables map buttons so user cannot change map while running
    btnMap1.config(state='disabled')
    btnMap2.config(state='disabled')
    btnMap3.config(state='disabled')
    btnMap4.config(state='disabled')

    global btnStopPressed
    btnStopPressed = False
    
    #Countdown function
    def counter_label(label):
      global countdown
      countdown = 61
      def count():
        global countdown
        global programRunning
        global ob1
        global ob2
        global ob3
        global ob4
        global ob5
        global canvas
        global btnStopPressed
        #Decrease countdown by 1
        countdown -= 1
        if countdown <= 0:
          programRunning = False
          #Enables buttons so user can change map once game has stopped
          btnMap1.config(state='normal')
          btnMap2.config(state='normal')
          btnMap3.config(state='normal')
          btnMap4.config(state='normal')
          #Message box to user, only shows if timer has run out
          if btnStopPressed == False:
              label.config(text=str(countdown))
              ctypes.windll.user32.MessageBoxA(0, "The timer has run out!", "Time up!", 0)
        elif countdown > 0:
          programRunning = True
          label.config(text=str(countdown))
          #after a thousand ticks call count function 
          label.after(1000, count)
          #random colour change of objects every 5 seconds
        if countdown % 5 == 0:
          # randomly select an object to turn green in the range
          green = random.randrange(1,5,1)
          if green == 1:
            canvas.itemconfig(ob1, fill='green', outline='green', width=3, tag="1")
            canvas.itemconfig(ob2, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob3, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob4, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob5, fill='red', outline='red', width=3, tag="0")
          elif green == 2:
            canvas.itemconfig(ob1, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob2, fill='green', outline='green', width=3, tag="1")
            canvas.itemconfig(ob3, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob4, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob5, fill='red', outline='red', width=3, tag ="0")
          elif green == 3:
            canvas.itemconfig(ob1, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob2, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob3, fill='green', outline='green', width=3, tag="1")
            canvas.itemconfig(ob4, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob5, fill='red', outline='red', width=3, tag="0")
          elif green == 4:
            canvas.itemconfig(ob1, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob2, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob3, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob4, fill='green', outline='green', width=3, tag="1")
            canvas.itemconfig(ob5, fill='red', outline='red', width=3, tag="0")
          elif green == 5:
            canvas.itemconfig(ob1, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob2, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob3, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob4, fill='red', outline='red', width=3, tag="0")
            canvas.itemconfig(ob5, fill='green', outline='green', width=3, tag="1")
      count()

    counter_label(label)
   

    #Define as a global variable once to keep using
    global programRunning
    programRunning = True

    while programRunning == True:  

        # create shape coordinates        
        r1x1, r1y1, r1x2, r1y2 = canvas.coords(rb1) # sides of rb1 object
        r2x1, r2y1, r2x2, r2y2 = canvas.coords(rb2) # side of rb1 object

        # robot 1 boundary detection and response
        if r1x1 <= x_min + 10: # robot has reached left side of screen
            r1vx = 10.0            
        if r1y1 <= y_min + 10: # robot has reached top side of screen
            r1vy = 5.0
        if r1x2 >= x_max - 10: # robot has reached right side of screen
            r1vx = -10.0
        if r1y2 >= y_max - 10: # robot has reached bottom side of screen
            r1vy = -5.0

        # robot 2 boundary detection and response
        if r2x1 <= x_min + 10: # robot has reached left side of screen
            r2vx = 10.0            
        if r2y1 <= y_min + 10: # robot has reached top side of screen
            r2vy = 5.0
        if r2x2 >= x_max - 10: # robot has reached right side of screen
            r2vx = -10.0
        if r2y2 >= y_max - 10: # robot has reached bottom side of screen
            r2vy = -5.0
             
        objList = [ob1, ob2, ob3, ob4, ob5] # list containing objects as elements
                
        for o in objList: # object detection and response

            x1, y1, x2, y2 = canvas.coords(o) # declare sides of objList element            
            objTag = str(canvas.gettags(o))
            objTag = int(objTag[2])
                        
            if objTag == 0:
                # robot 1
                if r1x1 > (x2 - 10) and r1x1 < (x2 + 10) and r1y1 > y1 and r1y1 < y2: # right side of object
                    if r1vy == 5.0 and r1vx == -10.0: # if approach from top right
                        r1vx = 10.0    
                    if r1vy == -5.0 and r1vx == -10.0: # if approach from bottom right
                        r1vx = 10.0                             
                                    
                if r1x2 < (x1 + 10) and r1x2 > (x1 - 10) and r1y1 > y1 and r1y2 < y2: # left side of object
                    if r1vy == 5.0 and r1vx == 10.0: # if approach from top right
                        r1vx = -10.0                    
                    if r1vy == -5.0 and r1vx == 10.0: # if approach from bottom right
                        r1vx = -10.0                    
                
                if r1y2 > (y1 - 10) and r1y2 < (y1 + 10) and r1x1 > x1 and r1x1 < x2: # top side of object
                    if r1vy == 5.0 and r1vx == 10.0: # if approach from top left
                        r1vy = -5.0                                           
                    if r1vy == 5.0 and r1vx == -10.0: # if approach from top right
                        r1vy = -5.0
                                                                
                if r1y1 < (y2 + 10) and r1y1 > (y2 - 10) and r1x1 > x1 and r1x1 < x2: # bottom side of object
                    if r1vy == -5.0 and r1vx == 10.0: # if approach from bottom left
                        r1vy = 5.0                                           
                    if r1vy == -5.0 and r1vx == -10.0: # if approach from bottom right
                        r1vy = 5.0
                        
                # robot 2
                if r2x1 > (x2 - 10) and r2x1 < (x2 + 10) and r2y1 > y1 and r2y1 < y2: # right side of object
                    if r2vy == 5.0 and r2vx == -10.0: # if approach from top right
                        r2vx = 10.0    
                    if r2vy == -5.0 and r2vx == -10.0: # if approach from bottom right
                        r2vx = 10.0                             
                                    
                if r2x2 < (x1 + 10) and r2x2 > (x1 - 10) and r2y1 > y1 and r2y2 < y2: # left side of object
                    if r2vy == 5.0 and r2vx == 10.0: # if approach from top right
                        r2vx = -10.0                    
                    if r2vy == -5.0 and r2vx == 10.0: # if approach from bottom right
                        r2vx = -10.0                    
                
                if r2y2 > (y1 - 10) and r2y2 < (y1 + 10) and r2x1 > x1 and r2x1 < x2: # top side of object
                    if r2vy == 5.0 and r2vx == 10.0: # if approach from top left
                        r2vy = -5.0                                           
                    if r2vy == 5.0 and r2vx == -10.0: # if approach from top right
                        r2vy = -5.0
                                                                
                if r2y1 < (y2 + 10) and r2y1 > (y2 - 10) and r2x1 > x1 and r2x1 < x2: # bottom side of object
                    if r2vy == -5.0 and r2vx == 10.0: # if approach from bottom left
                        r2vy = 5.0                                           
                    if r2vy == -5.0 and r2vx == -10.0: # if approach from bottom right
                        r2vy = 5.0
        
        # reposition moving objects
        canvas.coords(rb1, r1x1 + r1vx, r1y1 + r1vy, r1x2 + r1vx, r1y2 + r1vy)
        canvas.coords(rb2, r2x1 + r2vx, r2y1 + r2vy, r2x2 + r2vx, r2y2 + r2vy)
        canvas.update()

        # Sleep for 0.1 seconds, then delete the image.
        time.sleep(0.1)      

        #Incrementing intPlay
        intPlay = intPlay + 1
        
#Reset Function
def Reset():
    Stop()
    canvas.delete("all")
    global ButtonPressed
    ButtonPressed = 1

#Map Functions
def Map1():
    global ob1
    global ob2
    global ob3
    global ob4
    global ob5
    ob1=canvas.create_rectangle(100, 100, 200, 170, fill='red', outline='red', width=3, tag="0")
    ob2=canvas.create_rectangle(754, 100, 654, 170, fill='red', outline='red', width=3, tag="0")
    ob3=canvas.create_rectangle(550, 280, 300, 200, fill='red', outline='red', width=3, tag="0")
    ob4=canvas.create_rectangle(100, 380, 200, 310, fill='red', outline='red', width=3, tag="0")
    ob5=canvas.create_rectangle(754, 380, 654, 310, fill='red', outline='red', width=3, tag="0")

def Map2():
    global ob1
    global ob2
    global ob3
    global ob4
    global ob5
    ob1=canvas.create_rectangle(180, 140, 310, 85, fill='red', outline='red', width=3, tag="0")
    ob2=canvas.create_rectangle(550, 110, 800, 60, fill='red', outline='red', width=3, tag="0")
    ob3=canvas.create_rectangle(390, 190, 470, 400, fill='red', outline='red', width=3, tag="0")
    ob4=canvas.create_rectangle(50, 330, 330, 400, fill='red', outline='red', width=3, tag="0")
    ob5=canvas.create_rectangle(550, 330, 800, 400, fill='red', outline='red', width=3, tag="0")

def Map3():
    global ob1
    global ob2
    global ob3
    global ob4
    global ob5
    ob1=canvas.create_rectangle(60, 60, 130, 130, fill='red', outline='red', width=3, tag="0")
    ob2=canvas.create_rectangle(350, 100, 420, 350, fill='red', outline='red', width=3, tag="0")
    ob3=canvas.create_rectangle(500, 130, 790, 70, fill='red', outline='red', width=3, tag="0")
    ob4=canvas.create_rectangle(250, 440, 310, 390, fill='red', outline='red', width=3, tag="0")
    ob5=canvas.create_rectangle(490, 360, 790, 420, fill='red', outline='red', width=3, tag="0")

def Map4():
    global ob1
    global ob2
    global ob3
    global ob4
    global ob5
    ob1=canvas.create_rectangle(390, 60, 470, 120, fill='red', outline='red', width=3, tag="0")
    ob2=canvas.create_rectangle(190, 210, 270, 270, fill='red', outline='red', width=3, tag="0")
    ob3=canvas.create_rectangle(590, 210, 670, 270, fill='red', outline='red', width=3, tag="0")
    ob4=canvas.create_rectangle(390, 370, 470, 430, fill='red', outline='red', width=3, tag="0")
    ob5=canvas.create_rectangle(640, 370, 800, 430, fill='red', outline='red', width=3, tag="0")
    

#Loading map functions
def MapLoad1():
    canvas.delete("all")
    global gif1
    image1=canvas.create_image(0,0,image=gif1,anchor="nw",tag="img")
    Map1()
    global ButtonPressed
    ButtonPressed = 1
    
def MapLoad2():
    canvas.delete("all")
    global gif2
    image2=canvas.create_image(0,0,image=gif2,anchor="nw",tag="img")
    Map2()
    global ButtonPressed
    ButtonPressed = 2
    
def MapLoad3():
    canvas.delete("all")
    global gif3
    image3=canvas.create_image(0,0,image=gif3,anchor="nw",tag="img")
    Map3()
    global ButtonPressed
    ButtonPressed = 3
    
def MapLoad4():
    canvas.delete("all")
    global gif4
    image4=canvas.create_image(0,0,image=gif4,anchor="nw",tag="img")
    Map4()
    global ButtonPressed
    ButtonPressed = 4
                               
#Creating buttons
btnStart=Button(window, text='Start', height=1, width=20, command=Start)
btnStop=Button(window, text='Stop', height=1, width=20, command=Stop)
btnReset=Button(window, text='Reset', height=1, width=20, command=Reset)

#Places buttons in correct positions
btnStart.place(x=11, y=500)
btnStop.place(x=11, y=530)
btnReset.place(x=712, y=530)

#Creating countdown label
label= tk.Label(font=('Helvetica', 20), text = "0")
label.place(x=400, y=500)
label.pack()

#Creating image buttons
btnMap1=Button(window, text="1", height=1, width=2, command=MapLoad1)
btnMap2=Button(window, text="2", height=1, width=2, command=MapLoad2)
btnMap3=Button(window, text="3", height=1, width=2, command=MapLoad3)
btnMap4=Button(window, text="4", height=1, width=2, command=MapLoad4)

#Placement of image buttons
btnMap1.place(x=712, y=500)
btnMap2.place(x=754, y=500)
btnMap3.place(x=797, y=500)
btnMap4.place(x=837, y=500)

#Padds canvas
canvas.pack(padx=10,pady=10)

window.mainloop()
