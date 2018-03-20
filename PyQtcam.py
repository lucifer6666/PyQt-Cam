from tkinter import *
from PyQt4 import QtGui,QtCore
import cv2
class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setGeometry(150,150,680,565)
        self.setWindowTitle('Cam')
        self.video = QtGui.QLabel('', self)
        self.video.setGeometry(20, 20, 640, 485)
        self.btn1 = QtGui.QPushButton('Start', self)
        self.btn1.setGeometry(50, 515, 100, 30)
        self.btn1.clicked.connect(self.Start)
        self.btn3 = QtGui.QPushButton('Stop', self)
        self.btn3.setGeometry(170, 515, 100, 30)
        self.btn3.clicked.connect(self.Stop)
        self.btn4 = QtGui.QPushButton('Exit', self)
        self.btn4.setGeometry(290, 515, 100, 30)
        self.btn4.clicked.connect(self.Exit)
        myPixmap = QtGui.QPixmap("./img/camera.jpg")
        myScaledPixmap = myPixmap.scaled(self.video.size())
        self.video.setPixmap(myScaledPixmap)
        self.cap = cv2.VideoCapture(1)
        self.show()
    def Start(self):
        self.fps=30
        self.timer = QtCore.QTimer()
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video.setPixmap(pix)
        self.timer.timeout.connect(self.Start)
        self.timer.start(1000. / self.fps)
    def Stop(self):
        self.timer.stop()
    def Exit(self):
        sys.exit()
app=QtGui.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())