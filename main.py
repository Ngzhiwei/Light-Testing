from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
import serial

Arduino = serial.Serial('COM5', 9600)

root = Tk()

root.geometry('615x130')

estilo = ttk.Style()
estilo.theme_use('clam')

def Presionado(btn, luz):
    if btn['bg'] == '#F0F0F0':
        btn.config(bg='yellow')
        Arduino.write(f'on{luz}\r'.encode('ascii'))
        Arduino.flushInput()
        print(Arduino.readline().decode())
    else:
        btn.config(bg='#F0F0F0')
        Arduino.write(f'off{luz}\r'.encode('ascii'))
        Arduino.flushInput()
        print(Arduino.readline().decode())

def Arranque():
    global cantidadon1, cantidadon2, cantidadon3, cantidadon4, arranque, laburo
    laburo = root.after(1000, Arranque)

    if arranque == 0:
        botonarranque.config(text='Stop', bg='red', command=Stop)
        arranque = 1
    
    Arduino.write('111\r'.encode('ascii'))
    Arduino.flush()
    data = Arduino.readline().decode()

    print(data)
    print(data[4])
    print(data[6])
    print(data[8])
    print(data[10])
    cantidadon1 = cantidadon1 + int(data[4])
    cantidadluz1.config(text=str(cantidadon1))
    cantidadon2 = cantidadon2 + int(data[6])
    cantidadluz2.config(text=str(cantidadon2))
    cantidadon3 = cantidadon3 + int(data[8])
    cantidadluz3.config(text=str(cantidadon3))
    cantidadon4 = cantidadon4 + int(data[10])
    cantidadluz4.config(text=str(cantidadon4))


def Stop():
    global laburo, arranque
    root.after_cancel(laburo)
    botonarranque.config(text='Start', bg='green', command=Arranque)
    arranque = 0



laburo = 1
arranque = 0

tensionlinea = 220

cantidadon1 = 0
cantidadon2 = 0
cantidadon3 = 0
cantidadon4 = 0

seprarado = Label(root, text=' ').grid(row=0, column=0)
separador1 = Label(root, text=' ').grid(row=2, column=1)
separador2 = Label(root, text=' ').grid(row=2, column=3)
separador3 = Label(root, text=' ').grid(row=2, column=5)
separador4 = Label(root, text=' ').grid(row=2, column=7)
separador5 = Label(root, text=' ').grid(row=2, column=9)

tension = Label(root, text=f'Tensión: {str(tensionlinea)}' + 'V').grid(row=1, column=9)

cantidad = Label(root, text='Cant. veces encendida: ').grid(row=1, column= 1)
cantidadluz1 = ttk.Label(root, text=str(cantidadon1))
cantidadluz2 = ttk.Label(root, text=str(cantidadon2))
cantidadluz3 = ttk.Label(root, text=str(cantidadon3))
cantidadluz4 = ttk.Label(root, text=str(cantidadon4))

botonluz1 = Button(root, text='ON 1', bg='#F0F0F0', padx='20px', pady='7px', command=lambda: Presionado(botonluz1, 1))
botonluz2 = Button(root, text='ON 2', bg='#F0F0F0', padx='20px', pady='7px', command=lambda: Presionado(botonluz2, 2))
botonluz3 = Button(root, text='ON 3', bg='#F0F0F0', padx='20px', pady='7px', command=lambda: Presionado(botonluz3, 3))
botonluz4 = Button(root, text='ON 4', bg='#F0F0F0', padx='20px', pady='7px', command=lambda: Presionado(botonluz4, 4))

botonarranque = Button(root, text='Start', bg='green', command=Arranque)

cantidadluz1.grid(row=1, column= 2)
cantidadluz2.grid(row=1, column= 4)
cantidadluz3.grid(row=1, column= 6)
cantidadluz4.grid(row=1, column= 8)

botonarranque.grid(row=3, column=1)

botonluz1.grid(row=3, column=2)
botonluz2.grid(row=3, column=4)
botonluz3.grid(row=3, column=6)
botonluz4.grid(row=3, column=8)


root.mainloop()
