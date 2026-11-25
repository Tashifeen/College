
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6 import QtWidgets
import sys # means system

class Ui_MainWindow(QMainWindow): #subclass
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300) # (ax, ay, aw, ah)
        self.setWindowTitle("My first Window")
        
        self.setupUI()
        
    def setupUI(self):
        self.text = QLabel(self)
        self.text.setText("Hi this is my first code")
        self.text.move(50,50)
        
        # creating a button
        self.btn1 = QtWidgets.QPushButton(self) # (icon, text)
        self.btn1.setText("Click on me")
        self.btn1.clicked.connect(self.on_clicked) # connects function to when button 1 is clicked
                                     # only need to write name of function!
    def on_clicked(self):
        self.text.setText("This text has been changed")

def main():
    app = QApplication(sys.argv) # anytime an arg is passed through command line python it transfers this into q application using this system.argv
    # Passing sys.argv to QApplication allows the application to process command-line arguments that can be used to control the behavior of the GUI (e.g., opening the application in a specific mode).
    win = Ui_MainWindow()
    
    win.show()    
    sys.exit(app.exec())
    
main()