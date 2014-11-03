from Tkinter import *
import ttk
#Creating window and canvas
window = Tk()
canvas = Canvas(window, width=854, height=480, bg='white')
canvas.pack()
window.title('Sloths Virtual Robot')
window.geometry('{}x{}'. format(874,568))
window.resizable(width=FALSE, height=FALSE)

#Start Function
def Start():
  
#Stop Function
def Stop():

#Reset Function
def Reset():
  canvas.delete("all")
  lblTimer = Label(text = "00:00:00", font=('Helvetica', 20))
  #Add Stop timer/robot code
  #Add Remove robot code

#Creating buttons
btnStart=Button(window, text='Start', height=1, width=20, command=Start)
btnStop=Button(window, text='Stop', height=1, width=20, command=Stop)
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
