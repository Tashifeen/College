from PyQt6 import QtCore, QtGui, QtWidgets


class OCRWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None): # parent = None makes this widget a toplevel window, new window behaves independantly 
        super().__init__(parent) # Calls the constructor of the parent class
        self.setWindowTitle("OCRWindow")
        self.resize(398, 293)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        
        # Create a QLabel with a clickable link
        
        self.pmtLink = QtWidgets.QLabel('<a href="https://www.physicsandmathstutor.com/physics-revision/a-level-ocr-a/module-3/">Physics & Maths Tutor</a>', self.centralwidget)
        self.pmtLink.setGeometry(QtCore.QRect(10, 70, 281, 21))
        self.pmtLink.setObjectName("pmtLink")
        self.pmtLink.setOpenExternalLinks(True)  # Allow opening external links
        self.pmtLink.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.savemyexamsLink = QtWidgets.QLabel('<a href="https://www.savemyexams.com/a-level/physics/ocr/17/revision-notes/3-forces--motion/3-2-linear--projectile-motion/3-2-5-projectile-motion/">Save My Exams</a>', self.centralwidget)
        self.savemyexamsLink.setGeometry(QtCore.QRect(10, 110, 281, 21))
        self.savemyexamsLink.setObjectName("savemyexamsLink")
        self.savemyexamsLink.setOpenExternalLinks(True)
        self.savemyexamsLink.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.reviselyLink = QtWidgets.QLabel('<a href="https://www.revisely.com/alevel/physics/ocr/videos">Revisely</a>', self.centralwidget)
        self.reviselyLink.setGeometry(QtCore.QRect(10, 150, 281, 21))
        self.reviselyLink.setObjectName("reviselyLink")
        self.reviselyLink.setOpenExternalLinks(True)
        self.reviselyLink.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.cognitoLink = QtWidgets.QLabel('<a href="https://cognitoedu.org/coursesubtopic/p3-alevel-ocr_jIAaqmtI">Cognito</a>', self.centralwidget)
        self.cognitoLink.setGeometry(QtCore.QRect(10, 190, 281, 21))
        self.cognitoLink.setObjectName("cognitoLink")
        self.cognitoLink.setOpenExternalLinks(True)
        self.cognitoLink.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))    
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR A"))
        self.titleLabel.setText(_translate("MainWindow", "OCR A Revision Links"))
        # Remove link variables from this function so that they are not altered and can remain as links

