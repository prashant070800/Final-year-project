import sys
import cv2

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5 import QtWidgets, QtCore, QtGui

#https://ru.stackoverflow.com/a/1150993/396441

class Thread1(QThread):
    changePixmap = pyqtSignal(QImage)
    
    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap1.set(3,480)
        self.cap1.set(4,640)
        self.cap1.set(5,30)
        while True:
            ret1, image1 = self.cap1.read()
            if ret1:
                im1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = im1.shape
                step1 = channel1 * width1
                qImg1 = QImage(im1.data, width1, height1, step1, QImage.Format_RGB888)
                self.changePixmap.emit(qImg1)

class Thread2(QThread):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.active = True

    def run(self):
        if self.active:            
            self.fourcc = cv2.VideoWriter_fourcc(*'Random')
            self.out1 = cv2.VideoWriter('output.avi', self.fourcc, 30, (640,480))
            self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.cap1.set(3, 480)
            self.cap1.set(4, 640)
            self.cap1.set(5, 30)
            while self.active:                      
                ret1, image1 = self.cap1.read()
                if ret1:
                    self.out1.write(image1)     
                self.msleep(10)                      

    def stop(self):
        self.out1.release()

       
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(660, 520)
        self.control_bt = QPushButton('START')
        self.control_bt.clicked.connect(self.controlTimer)
        self.image_label = QLabel()
        self.saveTimer = QTimer()
        self.th1 = Thread1(self)
        self.th1.changePixmap.connect(self.setImage)
        self.th1.start()
        
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.image_label)
        vlayout.addWidget(self.control_bt)   

    @QtCore.pyqtSlot(QImage)
    def setImage(self, qImg1):
        self.image_label.setPixmap(QPixmap.fromImage(qImg1))

    def controlTimer(self):
        if not self.saveTimer.isActive():
            # write video
            self.saveTimer.start()
            self.th2 = Thread2(self)
            self.th2.active = True                                
            self.th2.start()
            # update control_bt text
            self.control_bt.setText("STOP")
        else:
            # stop writing
            self.saveTimer.stop()
            self.th2.active = False                   
            self.th2.stop()                         
            self.th2.terminate()                    
            # update control_bt text
            self.control_bt.setText("START")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
