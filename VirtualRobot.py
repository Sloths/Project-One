from Tkinter import *
import ttk
import random
import time

#Creating window and canvas
window = Tk()
canvas = Canvas(window, width=854, height=480, bg='white')
canvas.pack()
window.title('Sloths Virtual Robot')
window.geometry('{}x{}'. format(874,568))
window.resizable(width=FALSE, height=FALSE)

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

    # create robot
    rb1 = canvas.create_rectangle(40, 80, 40 + 10, 80 + 10, fill = "red")

    # create test obstacle
    ob_x1 = random.randint(0, 854 - 50) # generate random x1 value
    ob_y1 = random.randint(0, 480 - 50) # generate random y1 value
    ob1 = canvas.create_rectangle(ob_x1, ob_y1, ob_x1 + 50, ob_y1 + 50, fill = "green")

    programRunning = True

    while programRunning:  

        # create shape coordinates
        rx1, ry1, rx2, ry2 = canvas.coords(rb1) # robot
        ox1, oy1, ox2, oy2 = canvas.coords(ob1) # object

        # robot boundary detection and response
        if rx1 <= x_min + 10:
            vx = 10.0
        if ry1 <= y_min + 10:
            vy = 5.0
        if rx2 >= x_max - 10:
            vx = -10.0
        if ry2 >= y_max - 10:
            vy = -5.0

        # create count variables
        count = 0
        count_forward = 0

        # robot and object detection and response
        if rx1 > (ox2 - 10) and rx1 < (ox2 + 10) and ry1 < oy1 and ry1 > oy2: # right side of object
            count_forward = 5
        if rx2 < (ox1 + 10) and rx2 > (ox1 - 10) and ry1 > oy1 and ry2 < oy2: # left side of object
            count = 5
        if ry2 > (oy1 - 10) and ry2 < (oy1 + 10) and rx1 > ox1 and rx1 < ox2: # top side of object
            count_forward = 0
        if ry1 < (oy2 + 10) and ry1 > (oy2 - 10) and rx1 > ox1 and rx1 < ox2: # bottom side of object
            count = 5

        # action performed from count and count_forward
        if count > 0:
            vx = -10.0
            vy = 5.0
            count = count - 1
        if count_forward > 0:
            vx = 10.0
            vy = -5.0
            count_forward = count_forward - 1

        # reposition moving objects
        canvas.coords(rb1, rx1 + vx, ry1 + vy, rx2 + vx, ry2 + vy)
        canvas.update()

        # Sleep for 0.1 seconds, then delete the image.
        time.sleep(0.1)  


#Reset Function
def Reset():
  canvas.delete("all")
  lblTimer = Label(text = "00:00:00", font=('Helvetica', 20))
  #Add Stop timer/robot code
  #Add Remove robot code

#Creating buttons
btnStart=Button(window, text='Start', height=1, width=20, command=Start)
btnStop=Button(window, text='Stop', height=1, width=20)
btnReset=Button(window, text='Reset', height=1, width=20, command=Reset)

#Places buttons in correct positions
btnStart.place(x=11, y=500)
btnStop.place(x=11, y=530)
btnReset.place(x=712, y=530)

#Creating label and positioning
lblTimer=Label(text='00:00:00', font=('Helvetica', 20))
lblTimer.place(x=400, y=500)

#Creating ComboBox
cmbMap=ttk.Combobox(window, values=["Map 1", "Map 2", "Map 3", "Map 4", "Map 5", "Map 6"], height=1, width=21) #Add command once coded
cmbMap.place(x=712, y=500)

#Padds canvas
canvas.pack(padx=10,pady=10)

window.mainloop()
