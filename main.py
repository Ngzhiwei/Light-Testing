import sys, serial, time
from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
import serial.tools.list_ports

Arduino = serial.Serial('COM5',9600)

time.sleep(1)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowTitle('Test')
        self.button.clicked.connect(self.Temp)

    def Temp(self):
        tiempo = self.input.text()
        Arduino.write(tiempo.encode('ascii'))
        celsius = Arduino.readline()
        celsius = celsius.decode('utf-8')
        self.lcdlamp1a.display(celsius[0:5])
        self.lcdlamp2a.display(celsius[0:5])
        self.lcdlamp3a.display(celsius[0:5])
        self.lcdlamp4a.display(celsius[0:5])
        self.lcdlamp5a.display(celsius[0:5])
        self.lcdlamp6a.display(celsius[0:5])
        self.lcdlamp7a.display(celsius[0:5])
        self.lcdlamp8a.display(celsius[0:5])
        Arduino.reset_input_buffer()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
     QWidget {
        font-size: 15px;
     }
     ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')