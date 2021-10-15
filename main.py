from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
import serial

Arduino = serial.Serial('COM5',9600)

root = Tk() 
root.geometry('175x210')

cant = 0
maxconfigc = 150
maxconfigk = 373
maxconfigf = 212
celsius = 0
kelvin = 0
fahrenheit = 0

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("red.Vertical.TProgressbar", foreground='red', background='red')
estilo.configure("yellow.Vertical.TProgressbar", foreground='yellow', background='yellow')
estilo.configure("green.Vertical.TProgressbar", foreground='green', background='green')

def Decod(cadena):
    global celsius, kelvin, fahrenheit
    coma1 = cadena.index(',')
    celsius = cadena[0:coma1]
    coma2 = cadena.index(',', coma1+1)
    fahrenheit = cadena[coma1+1:coma2]
    kelvin = cadena[coma2+1:]

def Colores():
    if float(celsius) < 50:
        barra1.config(style='green.Vertical.TProgressbar')
        barra2.config(style='green.Vertical.TProgressbar')
        barra3.config(style='green.Vertical.TProgressbar')
    if float(celsius) > 50 and float(celsius) < 70:
        barra1.config(style='yellow.Vertical.TProgressbar')
        barra2.config(style='yellow.Vertical.TProgressbar')
        barra3.config(style='yellow.Vertical.TProgressbar')
    if float(celsius) > 70:
        barra1.config(style='red.Vertical.TProgressbar')
        barra2.config(style='red.Vertical.TProgressbar')
        barra3.config(style='red.Vertical.TProgressbar')

def HacerClick():

    global cant, celsius
    Arduino.write('10'.encode('ascii'))
    temperaturas = Arduino.readline().decode()
    Decod(temperaturas)
    Arduino.flushInput()
    Colores()
    barra1.config(value=celsius)
    barra2.config(value=fahrenheit)
    barra3.config(value=kelvin)
    tempc.config(text=celsius)
    tempf.config(text=fahrenheit)
    tempk.config(text=kelvin)

    if cant != 10:
        root.after(1050, HacerClick)
        cant +=1
    else:
        cant = 0

barra1 = ttk.Progressbar(root, orient='vertical', style="green.Vertical.TProgressbar", length=150, maximum=maxconfigc)
maximobarra1 = Label(root)
barra2 = ttk.Progressbar(root, orient='vertical', style="green.Vertical.TProgressbar", length=150, maximum=maxconfigf)
maximobarra2 = Label(root)
barra3 = ttk.Progressbar(root, orient='vertical', style="green.Vertical.TProgressbar", length=150, maximum=maxconfigk)
maximobarra3 = Label(root)

tempc = Label(root, text=celsius)
tempf = Label(root, text=fahrenheit)
tempk = Label(root, text=kelvin)

button = Button(root, text='tocame bb', command=HacerClick)

button.place(y=175, x=55)
tempc.place(y=155, x=50)
tempf.place(y=155, x=80)
tempk.place(y=155, x=110)
barra1.place(y=5,x=50)
barra2.place(y=5,x=80)
barra3.place(y=5,x=110)

root.mainloop()
