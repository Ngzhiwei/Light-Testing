from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
import serial

root = Tk()

root.geometry('575x100')

on1 = 0
on2 = 0
on3 = 0
on4 = 0

def Presionado(btn, prendido):
    global on1
    if on1 == 0:
        btn.config(bg='yellow')
        on1 = 1
    else:
        btn.config(bg='#F0F0F0')
        on1 = 0

corriente1 = 1250
corriente2 = 80
corriente3 = 250
corriente4 = 50
tensionlinea = 220

cantidadon1 = 0
cantidadon2 = 0
cantidadon3 = 0
cantidadon4 = 0

tension = Label(root, text='Tensión:').grid(row=0, column=6)
tensionvalor = Label(root, text=str(tensionlinea) + 'V').grid(row=0, column=7)

cantidad = Label(root, text='Cant. veces encendida: ').grid(row=0, column= 1)
cantidadluz1 = Label(root, text=str(cantidadon1)).grid(row=0, column= 2)
cantidadluz2 = Label(root, text=str(cantidadon2)).grid(row=0, column= 3)
cantidadluz3 = Label(root, text=str(cantidadon3)).grid(row=0, column= 4)
cantidadluz4 = Label(root, text=str(cantidadon4)).grid(row=0, column= 5)

corriente = Label(root, text='Corriente:').grid(row=1, column= 1)
corrienteluz1 = Label(root, text=str(corriente1) + 'mA').grid(row=1, column=2)
corrienteluz2 = Label(root, text=str(corriente2) + 'mA').grid(row=1, column=3)
corrienteluz3 = Label(root, text=str(corriente3) + 'mA').grid(row=1, column=4)
corrienteluz4 = Label(root, text=str(corriente4) + 'mA').grid(row=1, column=5)

botonluz1 = Button(root, text='ON 1', padx='20px', pady='7px', command=lambda: Presionado(botonluz1, on1))
botonluz2 = Button(root, text='ON 2', padx='20px', pady='7px')
botonluz3 = Button(root, text='ON 3', padx='20px', pady='7px')
botonluz4 = Button(root, text='ON 4', padx='20px', pady='7px')

botonluz1.grid(row=2, column=2)
botonluz2.grid(row=2, column=3)
botonluz3.grid(row=2, column=4)
botonluz4.grid(row=2, column=5)


root.mainloop()