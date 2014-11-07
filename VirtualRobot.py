from Tkinter import *
import ttk
import random
import time
import Tkinter as tk

#Creating window and canvas
window = Tk()
canvas = Canvas(window, width=854, height=480, bg='white')
canvas.pack()
window.title('Sloths Virtual Robot')
window.geometry('{}x{}'. format(874,568))
window.resizable(width=FALSE, height=FALSE)

#countdown is set to 61 seconds
countdown = 61

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
    ob1=canvas.create_rectangle(100, 100, 200, 170,fill='green', width=3)
    ob2=canvas.create_rectangle(754, 100, 654, 170,fill='green', width=3)
    ob3=canvas.create_rectangle(550, 280, 300, 200,fill='green', width=3)
    ob4=canvas.create_rectangle(100, 380, 200, 310,fill='green', width=3)
    ob5=canvas.create_rectangle(754, 380, 654, 310,fill='green', width=3)

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
        rx1, ry1, rx2, ry2 = canvas.coords(rb1) # robot
        o1x1, o1y1, o1x2, o1y2 = canvas.coords(ob1) # object 1
        o2x1, o2y1, o2x2, o2y2 = canvas.coords(ob2) # object 2
        o3x1, o3y1, o3x2, o3y2 = canvas.coords(ob3) # object 3
        o4x1, o4y1, o4x2, o4y2 = canvas.coords(ob4) # object 4
        o5x1, o5y1, o5x2, o5y2 = canvas.coords(ob5) # object 5

        # robot boundary detection and response
        if rx1 <= x_min + 10:
            vx = 10.0
        if ry1 <= y_min + 10:
            vy = 5.0
        if rx2 >= x_max - 10:
            vx = -10.0
        if ry2 >= y_max - 10:
            vy = -5.0
            
        ''' COLLISION RELATED CODE '''

        # robot boundary detection and response
        if rx1 <= x_min + 10:
            vx = 10.0
        if ry1 <= y_min + 10:
            vy = 5.0
        if rx2 >= x_max - 10:
            vx = -10.0
        if ry2 >= y_max - 10:
            vy = -5.0
        
        # robot and object 1 detection and response
        if rx1 > (o1x2 - 10) and rx1 < (o1x2 + 10) and ry1 > o1y1 and ry1 < o1y2: # right side of object
            if vy == 5.0 and vx == -10.0:
                vy = 5.0
                vx = 10.0                
            if vy == -5.0 and vx == -10.0:
                vy = -5.0
                vx = 10.0
                
            
        if rx2 < (o1x1 + 10) and rx2 > (o1x1 - 10) and ry1 > o1y1 and ry2 < o1y2: # left side of object
            if vy == 5.0 and vx == 10.0:
                vx = -10.0
                vy = 5.0                
            if vy == -5.0 and vx == 10.0:
                vx = -10.0
                vy = -5.0
            
        if ry2 > (o1y1 - 10) and ry2 < (o1y1 + 10) and rx1 > o1x1 and rx1 < o1x2: # top side of object
            if vx == 10.0 and vy == 5.0:
                vx = 10.0
                vy = -5.0
            if vx == -10.0 and vy == 5.0:
                vx = -10.0
                vy = -5.0
                
        if ry1 < (o1y2 + 10) and ry1 > (o1y2 - 10) and rx1 > o1x1 and rx1 < o1x2: # bottom side of object
            if vx == 10.0 and vy == -5.0:
                vx = 10.0
                vy = 5.0
            if vx == -10.0 and vy == -5.0:
                vx = -10.0
                vy = 5.0

        # robot and object 2 detection and response
        if rx1 > (o2x2 - 10) and rx1 < (o2x2 + 10) and ry1 > o2y1 and ry1 < o2y2: # right side of object
            if vy == 5.0 and vx == -10.0:
                vy = 5.0
                vx = 10.0                
            if vy == -5.0 and vx == -10.0:
                vy = -5.0
                vx = 10.0
            
        if rx2 < (o2x1 + 10) and rx2 > (o2x1 - 10) and ry1 > o2y1 and ry2 < o2y2: # left side of object
            if vy == 5.0 and vx == 10.0:
                vx = -10.0
                vy = 5.0                
            if vy == -5.0 and vx == 10.0:
                vx = -10.0
                vy = -5.0
            
        if ry2 > (o2y1 - 10) and ry2 < (o2y1 + 10) and rx1 > o2x1 and rx1 < o2x2: # top side of object
            if vx == 10.0 and vy == 5.0:
                vx = 10.0
                vy = -5.0
            if vx == -10.0 and vy == 5.0:
                vx = -10.0
                vy = -5.0
                
        if ry1 < (o2y2 + 10) and ry1 > (o2y2 - 10) and rx1 > o2x1 and rx1 < o2x2: # bottom side of object
            if vx == 10.0 and vy == -5.0:
                vx = 10.0
                vy = 5.0
            if vx == -10.0 and vy == -5.0:
                vx = -10.0
                vy = 5.0

        # robot and object 3 detection and response
        if rx1 > (o3x2 - 10) and rx1 < (o3x2 + 10) and ry1 > o3y1 and ry1 < o3y2: # right side of object
            if vy == 5.0 and vx == -10.0:
                vy = 5.0
                vx = 10.0                
            if vy == -5.0 and vx == -10.0:
                vy = -5.0
                vx = 10.0
            
        if rx2 < (o3x1 + 10) and rx2 > (o3x1 - 10) and ry1 > o3y1 and ry2 < o3y2: # left side of object
            if vy == 5.0 and vx == 10.0:
                vx = -10.0
                vy = 5.0                
            if vy == -5.0 and vx == 10.0:
                vx = -10.0
                vy = -5.0
            
        if ry2 > (o3y1 - 10) and ry2 < (o3y1 + 10) and rx1 > o3x1 and rx1 < o3x2: # top side of object
            if vx == 10.0 and vy == 5.0:
                vx = 10.0
                vy = -5.0
            if vx == -10.0 and vy == 5.0:
                vx = -10.0
                vy = -5.0
                
        if ry1 < (o3y2 + 10) and ry1 > (o3y2 - 10) and rx1 > o3x1 and rx1 < o3x2: # bottom side of object
            if vx == 10.0 and vy == -5.0:
                vx = 10.0
                vy = 5.0
            if vx == -10.0 and vy == -5.0:
                vx = -10.0
                vy = 5.0

        # robot and object 4 detection and response
        if rx1 > (o4x2 - 10) and rx1 < (o4x2 + 10) and ry1 > o4y1 and ry1 < o4y2: # right side of object
            if vy == 5.0 and vx == -10.0:
                vy = 5.0
                vx = 10.0                
            if vy == -5.0 and vx == -10.0:
                vy = -5.0
                vx = 10.0
            
        if rx2 < (o4x1 + 10) and rx2 > (o4x1 - 10) and ry1 > o4y1 and ry2 < o4y2: # left side of object
            if vy == 5.0 and vx == 10.0:
                vx = -10.0
                vy = 5.0                
            if vy == -5.0 and vx == 10.0:
                vx = -10.0
                vy = -5.0
            
        if ry2 > (o4y1 - 10) and ry2 < (o4y1 + 10) and rx1 > o4x1 and rx1 < o4x2: # top side of object
            if vx == 10.0 and vy == 5.0:
                vx = 10.0
                vy = -5.0
            if vx == -10.0 and vy == 5.0:
                vx = -10.0
                vy = -5.0
                
        if ry1 < (o4y2 + 10) and ry1 > (o4y2 - 10) and rx1 > o4x1 and rx1 < o4x2: # bottom side of object
            if vx == 10.0 and vy == -5.0:
                vx = 10.0
                vy = 5.0
            if vx == -10.0 and vy == -5.0:
                vx = -10.0
                vy = 5.0

        # robot and object 5 detection and response
        if rx1 > (o5x2 - 10) and rx1 < (o5x2 + 10) and ry1 > o5y1 and ry1 < o5y2: # right side of object
            if vy == 5.0 and vx == -10.0:
                vy = 5.0
                vx = 10.0                
            if vy == -5.0 and vx == -10.0:
                vy = -5.0
                vx = 10.0
            
        if rx2 < (o5x1 + 10) and rx2 > (o5x1 - 10) and ry1 > o5y1 and ry2 < o5y2: # left side of object
            if vy == 5.0 and vx == 10.0:
                vx = -10.0
                vy = 5.0                
            if vy == -5.0 and vx == 10.0:
                vx = -10.0
                vy = -5.0
            
        if ry2 > (o5y1 - 10) and ry2 < (o5y1 + 10) and rx1 > o5x1 and rx1 < o5x2: # top side of object
            if vx == 10.0 and vy == 5.0:
                vx = 10.0
                vy = -5.0
            if vx == -10.0 and vy == 5.0:
                vx = -10.0
                vy = -5.0
                
        if ry1 < (o5y2 + 10) and ry1 > (o5y2 - 10) and rx1 > o5x1 and rx1 < o5x2: # bottom side of object
            if vx == 10.0 and vy == -5.0:
                vx = 10.0
                vy = 5.0
            if vx == -10.0 and vy == -5.0:
                vx = -10.0
                vy = 5.0

        # reposition moving objects
        canvas.coords(rb1, rx1 + vx, ry1 + vy, rx2 + vx, ry2 + vy)
        canvas.update()

        # Sleep for 0.1 seconds, then delete the image.
        time.sleep(0.1)  
    

#Reset Function
def Reset():
    canvas.delete("all") 

#Map 1 Function
def Map1():
    canvas.delete("all")
    ob1=canvas.create_rectangle(100, 100, 200, 170,fill='white', width=3)
    ob2=canvas.create_rectangle(754, 100, 654, 170,fill='white', width=3)
    ob3=canvas.create_rectangle(550, 280, 300, 200,fill='white', width=3)
    ob4=canvas.create_rectangle(100, 380, 200, 310,fill='white', width=3)
    ob5=canvas.create_rectangle(754, 380, 654, 310,fill='white', width=3)

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

#Creating ComboBox
cmbMap=ttk.Combobox(window, values=["Map 1", "Map 2", "Map 3", "Map 4", "Map 5", "Map 6"], height=1, width=21) #Add command once coded
cmbMap.place(x=712, y=500)

#Padds canvas
canvas.pack(padx=10,pady=10)

window.mainloop()
