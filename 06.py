
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QHBoxLayout, QGridLayout, QLabel, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)
        #
        # # lcd = QLCDNumber(self)
        # # sld = QSlider(Qt.Vertical, self)
        # #
        # # hbox = QHBoxLayout()
        # # hbox.addWidget(lcd)
        # # hbox.addWidget(sld)
        #
        # self.setLayout(vbox)
        # # self.setLayout(hbox)
        # sld.valueChanged.connect(lcd.display)

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {}, y: {}".format(x,y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Signal and Slot")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {}, y: {}".format(x, y)
        self.label.setText(text)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())