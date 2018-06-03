import random
# noinspection PyUnresolvedReferences
import tkinter as tk
# noinspection PyUnresolvedReferences
from tkinter import *
# noinspection PyUnresolvedReferences
import serial  # Serial imported for Serial communication
# noinspection PyUnresolvedReferences
import time  # Required to use delay functions
# noinspection PyUnresolvedReferences
from tkinter.messagebox import *  #reqd
# noinspection PyUnresolvedReferences
from time import sleep
# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import Adafruit_DHT
# noinspection PyUnresolvedReferences
import RPi.GPIO as IO
# noinspection PyUnresolvedReferences  
import time
import datetime

pinList = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]





     


IO.setwarnings(False)
IO.setmode (IO.BCM)           
IO.setup(25,IO.OUT)
IO.setup(8,IO.OUT)
IO.setup(26,IO.OUT)
IO.output(26,IO.HIGH)
IO.setup(19, IO.OUT)
IO.setup(26, IO.OUT)
IO.setup(4, IO.OUT)
IO.setup(17, IO.OUT)
IO.setup(24, IO.OUT)
IO.setup(27, IO.OUT)
IO.setup(22, IO.OUT)
IO.setup(10, IO.OUT)
IO.setup(9, IO.OUT)
IO.setup(11, IO.OUT)
IO.setup(5, IO.OUT)
IO.setup(6, IO.OUT)
IO.setup(13, IO.OUT)
IO.setup(2, IO.OUT)
IO.setup(18, IO.OUT)
IO.setup(23, IO.OUT)
IO.setup(3, IO.OUT)
IO.output(2,IO.HIGH)
IO.output(3,IO.HIGH)
IO.output(4,IO.HIGH)
IO.output(17,IO.HIGH)
IO.output(27,IO.HIGH)
IO.output(22,IO.HIGH)
IO.output(10,IO.HIGH)
IO.output(9,IO.HIGH)
IO.output(11,IO.HIGH)
IO.output(5,IO.HIGH)
IO.output(6,IO.HIGH)
IO.output(13,IO.HIGH)
IO.output(19,IO.HIGH)
IO.output(18,IO.HIGH)
IO.output(23,IO.HIGH)


p = IO.PWM(8,50)


window = tk.Tk()
window.wm_title("GRAPHICAL USER INTERFACE")
window.geometry("1400x1000")
window.config(bg="Black")
#window.iconbitmap("C:\\Users\\HP\\Desktop\\abhi\\icon.ico").....i will send file later to change ico 
window.tk_focusNext()


def led_on_off():
    if(IO.input(18)==1):
        print ("A")
        IO.output(18,IO.LOW)
        led = Button(btnFrame, text="PRESS TO TURN LED OFF", bg="WHITE",width=40,command=led_on_off)
        led.grid(row=15, column=0, padx=40, pady=10)
        
    else:
        IO.output(18,IO.HIGH)
        led = Button(btnFrame, text="PRESS TO TURN LED ON", bg="WHITE",width=40,command=led_on_off)
        led.grid(row=15, column=0, padx=40, pady=10)

def motor():
    while 1:
        p.start(7.5)                                                               
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)# change duty cycle for getting the servo position to 180º
        p.ChangeDutyCycle(2.5)
        time.sleep(1)# change duty cycle for getting the servo position to 0º

        

i20=0;
def counter20():
    global i20
    i20=i20+1
    if (i20%2==0):
        Temperature_Humidity = Button(btnFrame, width=40,text="STATUS OF TEMPERATURE AND HUMIDITY SENSOR OFF", command=counter20,bg="WHITE")
        Temperature_Humidity.grid(row=5, column=0, padx=40, pady=10)
        print (i20)
        temperature_humidity_off()
        
    else:
        Temperature_Humidity = Button(btnFrame, width=40,text="TEMPERATURE AND HUMIDITY SENSOR Working", command=counter20,bg="WHITE")
        Temperature_Humidity.grid(row=5, column=0, padx=40, pady=10)
        print (i20)
        temperature_humidity_on()
    
flag20=0;
def temperature_humidity_on():
    global flag20
    global i20
    if(i20%2==0):
        print("Off")
        IO.output(23,IO.HIGH)
    else:
        print("ON")
        now=datetime.datetime.now() 
        humidity, temperature = Adafruit_DHT.read_retry(11, 24)
        temperature_display=temperature
        humidity_display=humidity
        output='humidity='+str(humidity_display)+'%'+'  '+'temperature'+str(temperature_display)+'C'+'\n'+str(now)+'\n'
        print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
        sensor.insert(tk.END,str(output))
        if(temperature>25):
            IO.output(23,IO.LOW)
        else:
            IO.output(23,IO.HIGH)
    time.sleep(5)
    flag20=window.after(3,temperature_humidity_on)
    
def temperature_humidity_off():
    IO.output(23,IO.HIGH)
    
                
    
def delete_valve():
    valve.config(state=tk.NORMAL)
    valve.delete(1.0, tk.END)
    valve.config(state=tk.DISABLED)
    valve.config(state=tk.NORMAL)
#
def delete_sensor():
     sensor.config(state=tk.NORMAL)
     sensor.delete(1.0, tk.END)
     sensor.config(state=tk.DISABLED)
     sensor.config(state=tk.NORMAL)


def callback():
    print("a")

i1=0;
def counter1():
    global i1
    i1=i1+1
    if (i1%2==0):
        button11 = Button(left_button, text="GREEN1 OFF", width=8,command=counter1,bg="white",fg="RED")
        button11.grid(row=0, column=0,padx=40,pady=2)
    else:
        button11 = Button(left_button, text="GREEN1 On", width=8,command=counter1,bg="white",fg="RED")
        button11.grid(row=0, column=0,padx=40,pady=2)
        
    relay1()
    
flag1=0;
def relay1():
    global flag1
    if(i1%2==0):
        IO.output(19,IO.HIGH)
    else:
        if(i1%2!=0):
            print("ON")
            IO.output(19,IO.LOW)
            time.sleep(3)
            IO.output(19,IO.HIGH)
            time.sleep(3)
    flag1=window.after(3,relay1)

i2=0;
def counter2():
    global i2
    i2=i2+1
    if (i2%2==0):
        button22 = Button(left_button, text="GREEN2 OFF", width=8,command=counter2,bg="white",fg="RED")
        button22.grid(row=0, column=2,padx=40,pady=2)
    else:
        button22 = Button(left_button, text="GREEN2 On", width=8,command=counter2,bg="white",fg="RED")
        button22.grid(row=0, column=2,padx=40,pady=2)
    relay2()
    
flag2=0;
def relay2():
    global flag2
    if(i2%2==0): 
        IO.output(26,IO.HIGH)
    else:
        if(i2%2!=0):
            IO.output(26,IO.LOW)
            time.sleep(3)
            IO.output(26,IO.HIGH)
            time.sleep(3)
    flag2=window.after(3,relay2)

i3=0;
def counter3():
    global i3
    i3=i3+1
    if (i3%2==0):
        button33 = Button(left_button, text="GREEN3 OFF", width=8,command=counter3,bg="white",fg="RED")
        button33.grid(row=0, column=4,padx=40,pady=2)
    else:
        button33 = Button(left_button, text="GREEN3 On", width=8,command=counter3,bg="white",fg="RED")
        button33.grid(row=0, column=4,padx=40,pady=2)
    relay3()
    
flag3=0;
def relay3():
    global flag3
    if(i3%2==0):
        #valve.insert(tk.END,'Green Valve 3 switched off')
        IO.output(4,IO.HIGH)
    else:
        if(i3%2!=0):
         #   valve.insert(tk.END,'Green Valve 3 Working')
            IO.output(4,IO.LOW)
            time.sleep(3)
            IO.output(4,IO.HIGH)
            time.sleep(3)
    flag3=window.after(3,relay3)

i4=0;
def counter4():
    global i4
    i4=i4+1
	if (i1%2==0):
        button44 = Button(left_button, text="GREEN4 OFF", width=8,command=counter4,bg="white",fg="RED")
        button44.grid(row=0, column=6,padx=40,pady=2)
    else:
        button44 = Button(left_button, text="GREEN4 On", width=8,command=counter4,bg="white",fg="RED")
        button44.grid(row=0, column=6,padx=40,pady=2)
	
    relay4()
    
flag4=0;
def relay4():
    global flag4
    if(i4%2==0):
        #valve.insert(tk.END,'Green Valve 4 switched off')
        IO.output(17,IO.HIGH)
    else:
        if(i4%2!=0):
         #   valve.insert(tk.END,'Green Valve 4 Working')
            IO.output(17,IO.LOW)
            time.sleep(3)
            IO.output(17,IO.HIGH)
            time.sleep(3)
    flag4=window.after(3,relay4)

i5=0;
def counter5():
    global i5
    i5=i5+1
	if (i1%2==0):
        button55 = Button(left_button, text="GREEN5 OFF", width=8,command=counter5,bg="white",fg="RED")
        button55.grid(row=0, column=8,padx=40,pady=2)
    else:
        button55 = Button(left_button, text="GREEN5 On", width=8,command=counter5,bg="white",fg="RED")
        button55.grid(row=0, column=8,padx=40,pady=2)
    relay5()
    
flag5=0;
def relay5():
    global flag5
    if(i5%2==0):
        #valve.insert(tk.END,'Green Valve 5 switched off')
        IO.output(27,IO.HIGH)
    else:
        if(i5%2!=0):
         #   valve.insert(tk.END,'Green Valve 5 Working')
            IO.output(27,IO.LOW)
            time.sleep(3)
            IO.output(27,IO.HIGH)
            time.sleep(3)
    flag5=window.after(3,relay5)

i6=0;
def counter6():
    global i6
    i6=i6+1
	if (i1%2==0):
        button11 = Button(left_button, text="GREEN6 OFF", width=8,command=counter6,bg="white",fg="RED")
        button11.grid(row=0, column=10,padx=40,pady=2)
    else:
        button66 = Button(left_button, text="GREEN6 On", width=8,command=counter6,bg="white",fg="RED")
        button66.grid(row=0, column=10,padx=40,pady=2)
    relay6()
    
flag6=0;
def relay6():
    global flag6
    if(i6%2==0):
        #valve.insert(tk.END,'Green Valve 6 switched off')
        IO.output(22,IO.HIGH)
    else:
        if(i6%2!=0):
         #   valve.insert(tk.END,'Green Valve 6 Working')
            IO.output(22,IO.LOW)
            time.sleep(3)
            IO.output(22,IO.HIGH)
            time.sleep(3)
    flag6=window.after(3,relay6)

i7=0;
def counter7():
    global i7
    i7=i7+1
	if (i7%2%2==0):
        button1 = Button(left_button, text="GROW1 OFF", width=8,command=counter7,bg="white",fg="RED")
        button11.grid(row=0, column=0,padx=40,pady=2)
    else:
        button1 = Button(left_button, text="GROW2 On", width=8,command=counter7,bg="white",fg="RED")
        button1.grid(row=0, column=0,padx=40,pady=2)
    relay7()
    
flag7=0;
def relay7():
    global flag7
    if(i7%2==0):
        #valve.insert(tk.END,'Grow Valve 1 switched off')
        IO.output(10,IO.HIGH)
    else:
        if(i7%2!=0):
         #   valve.insert(tk.END,'Grow Valve 1 Working')
            IO.output(10,IO.LOW)
            time.sleep(3)
            IO.output(10,IO.HIGH)
            time.sleep(3)
    flag7=window.after(3,relay7)

i8=0;
def counter8():
    global i8
    i8=i8+1
	if (i8%2%2%2==0):
        button2 = Button(left_button, text="GROW2 OFF", width=8,command=counter8,bg="white",fg="RED")
        button11.grid(row=0, column=1,padx=40,pady=2)
    else:
        button2 = Button(left_button, text="GROW2 On", width=8,command=counter8,bg="white",fg="RED")
        button11.grid(row=0, column=1,padx=40,pady=2)
    relay8()
    
flag8=0;
def relay8():
    global flag8
    if(i8%2==0):
        #valve.insert(tk.END,'Grow Valve 2 switched off')
        IO.output(9,IO.HIGH)
    else:
        if(i8%2!=0):
         #   valve.insert(tk.END,'Grow Valve 2 Working')
            IO.output(9,IO.LOW)
            time.sleep(3)
            IO.output(9,IO.HIGH)
            time.sleep(3)
    flag8=window.after(3,relay8)

i9=0;
def counter9():
    global i9
    i9=i9+1
	if (i9%2==0):
        button3 = Button(left_button, text="GROW3 OFF", width=8,command=counter9,bg="white",fg="RED")
        button3.grid(row=0, column=3,padx=40,pady=2)
    else:
        button3 = Button(left_button, text="GROW3 On", width=8,command=counter9,bg="white",fg="RED")
        button3.grid(row=0, column=3,padx=40,pady=2)
    relay9()
    
flag9=0;
def relay9():
    global flag9
    if(i9%2==0):
        #valve.insert(tk.END,'Grow Valve 3 switched off')
        IO.output(11,IO.HIGH)
    else:
        if(i9%2!=0):
         #   valve.insert(tk.END,'Grow Valve 3 Working')
            IO.output(11,IO.LOW)
            time.sleep(3)
            IO.output(11,IO.HIGH)
            time.sleep(3)
    flag9=window.after(3,relay9)

i10=0;
def counter10():
    global i10
    i10=i10+1
	if (i10%2==0):
        button4 = Button(left_button, text="GROW4 OFF", width=8,command=counter10,bg="white",fg="RED")
        button4.grid(row=0, column=3,padx=40,pady=2)
    else:
        button4 = Button(left_button, text="GROW4 On", width=8,command=counter10,bg="white",fg="RED")
        button4.grid(row=0, column=4,padx=40,pady=2)
    relay10()
    
flag10=0;
def relay10():
    global flag10
    if(i10%2==0):
        #valve.insert(tk.END,'Grow Valve 4 switched off')
        IO.output(5,IO.HIGH)
    else:
        if(i10%2!=0):
         #   valve.insert(tk.END,'Grow Valve 4 Working')
            IO.output(5,IO.LOW)
            time.sleep(3)
            IO.output(5,IO.HIGH)
            time.sleep(3)
    flag10=window.after(3,relay10)

i11=0;
def counter11():
    global i11
    i11=i11+1
	if (i11%2==0):
        button5 = Button(left_button, text="GROW5 OFF", width=8,command=counter11,bg="white",fg="RED")
        button5.grid(row=0, column=5,padx=40,pady=2)
    else:
        button3 = Button(left_button, text="GROW5 On", width=8,command=counter11,bg="white",fg="RED")
        button3.grid(row=0, column=5,padx=40,pady=2)
    relay11()
    
flag11=0;
def relay11():
    global flag11
    if(i11%2==0):
        #valve.insert(tk.END,'Grow Valve 5 switched off')
        IO.output(6,IO.HIGH)
        button5 = Button(left_button, text="GROW5 OFF", width=5,command=counter1,bg="white",fg="RED")
    else:
        if(i11%2!=0):
         #   valve.insert(tk.END,'Grow Valve 5 Working')
            IO.output(6,IO.LOW)
            button5 = Button(left_button, text="GROW5 ON", width=5,command=counter1,bg="white",fg="RED")
            time.sleep(3)
            IO.output(6,IO.HIGH)
            time.sleep(3)
    flag11=window.after(3,relay11)

i12=0;
def counter12():
    global i12
    i12=i12+1
	if (i12%2==0):
        button6 = Button(left_button, text="GROW6 OFF", width=8,command=counter12,bg="white",fg="RED")
        button6.grid(row=0, column=6,padx=40,pady=2)
    else:
        button3 = Button(left_button, text="GROW6 On", width=8,command=counter12,bg="white",fg="RED")
        button3.grid(row=0, column=6,padx=40,pady=2)
    relay12()
    
flag12=0;
def relay12():
    global flag12
    if(i12%2==0):
        #valve.insert(tk.END,'Grow Valve 6 switched off')
        IO.output(13,IO.HIGH)
        button6 = Button(left_button, text="GROW6 OFF", width=5,command=counter1,bg="white",fg="RED")
    else:
        if(i12%2!=0):
         #   valve.insert(tk.END,'Grow Valve 6 Working')
            IO.output(13,IO.LOW)
            button6 = Button(left_button, text="GROW6 OFF", width=5,command=counter1,bg="white",fg="RED")
            time.sleep(3)
            IO.output(13,IO.HIGH)
            time.sleep(3)
    flag12=window.after(3,relay12)


leftFrame = Frame(window, width=700, height = 1000, bg="BLACK", highlightthickness=0, highlightbackground="BLACK")
leftFrame.grid(row=0, column=0, padx=10, pady=2, sticky=N+S)

instructions = "AUTOMATED GREEN-HOUSE SYSTEM"
Instruct = Label(leftFrame, width=40, height=2, text=instructions, takefocus=10, wraplength=5090, anchor=W, justify=LEFT, font=("Verdana", 20),bg="GREY")
Instruct.grid(row=1, column=0, padx=1, pady=2)

left_button = Frame(leftFrame, width=700, height = 500, bg="BLACK")
left_button.grid(row=12, column=0, padx=10, pady=20)

left_canvas = Frame(leftFrame, width=700, height =500, bg="black")
left_canvas.grid(row=13,column=0,padx=40,pady=4)

button11 = Button(left_button, text="GREEN1", width=5,command=counter1,bg="white",fg="RED")
button11.grid(row=0, column=0,padx=40,pady=2)
circleCanvas11 = Canvas(left_canvas, width=60,height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas11.grid(row=25, column=0, padx=40, pady=2)

button22 = Button(left_button, text="GREEN2", width=5, command=counter2,bg="white",fg="RED")
button22.grid(row=0, column=2,padx=40,pady=2)
circleCanvas22 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas22.grid(row=25, column=1, padx=40, pady=2)

button33 = Button(left_button, text="GREEN3", width=5, command=counter3,bg="white",fg="RED")
button33.grid(row=0, column=4,padx=40,pady=2)
circleCanvas33 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas33.grid(row=25, column=2, padx=40, pady=2)

button44 = Button(left_button, text="GREEN4", width=5, command=counter4,bg="white",fg="RED")
button44.grid(row=0, column=6,padx=40,pady=2)
circleCanvas44 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas44.grid(row=25, column=3, padx=40, pady=2)

button55 = Button(left_button, text="GREEN5", width=5, command=counter5,bg="white",fg="RED")
button55.grid(row=0, column=8,padx=40,pady=2)
circleCanvas55 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas55.grid(row=25, column=4, padx=40, pady=2)


button66 = Button(left_button, text="GREEN6", width=5, command=counter6,bg="white",fg="RED")
button66.grid(row=0, column=10,padx=40,pady=2)
circleCanvas55 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas55.grid(row=25, column=5, padx=40, pady=2)



button1 = Button(left_button, text="GROW1", width=5, command=counter7,bg="white",fg="RED")
button1.grid(row=10, column=0,pady=2,padx=40)
circleCanvas1 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas1.grid(row=45, column=0, padx=40, pady=2)

button2 = Button(left_button, text="GROW2", width=5, command=counter8,bg="white",fg="RED")
button2.grid(row=10, column=2,padx=40,pady=2)
circleCanvas2 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas2.grid(row=45, column=1, padx=40, pady=2)


button3 = Button(left_button, text="GROW3", width=5, command=counter9,bg="white",fg="RED")
button3.grid(row=10, column=4,padx=40,pady=2)
circleCanvas3 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas3.grid(row=45, column=2, padx=40, pady=2)

button4 = Button(left_button, text="GROW4", width=5, command=counter10,bg="white",fg="RED")
button4.grid(row=10, column=6,padx=40,pady=2)
circleCanvas4 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas4.grid(row=45, column=3, padx=40, pady=2)

button5 = Button(left_button, text="GROW5", width=5, command=counter11,bg="white",fg="RED")
button5.grid(row=10, column=8,padx=40,pady=2)
circleCanvas5 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas5.grid(row=45, column=4, padx=40, pady=2)


button6 = Button(left_button, text="GROW6", width=5, command=counter12,bg="white",fg="RED")
button6.grid(row=10, column=10,padx=40,pady=2)
circleCanvas5 = Canvas(left_canvas, width=60, height=40, bg='grey', highlightthickness=1, highlightbackground="#333")
circleCanvas5.grid(row=45, column=5, padx=40, pady=2)




valve = tk.Text(leftFrame,height=20, width=80,font=('Verdana',12),bg="White")
valve.grid(column=0, row=400,pady=10)
valve.insert(tk.END,"status of valves\n ")

rightFrame = Frame(window, width=700, height = 600, bg="black", highlightthickness=2, highlightbackground="BLACK")
rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky=N+S)

btnFrame = Frame(rightFrame, width=70, height = 20, bg="BLACK")
btnFrame.grid(row=0, column=0, padx=0, pady=0)

sensor_delete = Button(rightFrame, width=40,text="CLEAR SENSOR LOG", command=delete_sensor,bg="WHITE")
sensor_delete.grid(row=25, column=0, padx=40, pady=10)

quit_program = Button(rightFrame, width=40,text="QUIT APPLICATION", command=quit,bg="WHITE")
quit_program.grid(row=40, column=0, padx=40, pady=10)

Temperature_Humidity= Button(btnFrame, width=40,text="CONTROL OF TEMPERATURE AND HUMIDITY", command=counter20,bg="WHITE")
Temperature_Humidity.grid(row=5, column=0, padx=40, pady=10)

light = Button(btnFrame, text="STATUS OF LIGHT SENSOR",width=40, bg="WHITE")
light.grid(row=10, column=0, padx=40, pady=10)

led = Button(btnFrame, text="LED CONTROL", bg="WHITE",width=40,command=led_on_off)
led.grid(row=15, column=0, padx=40, pady=10)

#led = Button(btnFrame, text="LED CONTROL", bg="WHITE",width=40,command=led_on_off)
#led.grid(row=35, column=0, padx=40, pady=10)

roof=Button(btnFrame,text="ROOF CONTROL",bg="WHITE",width=40,command=motor)
roof.grid(row=20,column=0,padx=40,pady=10)

button_delete_left = Button(rightFrame, text="CLEAR VALVE LOG", width=40, command=delete_valve,bg="white")
button_delete_left.grid(row=30, column=0,padx=40,pady=10)

sensor = tk.Text(rightFrame,height=20, width=30,font=('Verdana',12),bg="WHITE")
sensor.grid(column=0, row=45,pady=5,padx=0)
sensor.insert(tk.END,"SENSOR \n ")

window.mainloop()




