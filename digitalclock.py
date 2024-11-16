import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.timer = QTimer()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,400,200,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #24ff00")
        
        font_id = QFontDatabase.addApplicationFont("DS-DIGIB.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.label.setFont(my_font)
        
        self.setStyleSheet("background-color: #000000;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
