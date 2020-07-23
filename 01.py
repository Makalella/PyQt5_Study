
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Click", self)
        btn.resize(btn.sizeHint())  # 글씨를 기준으로 공간을 띄움
        btn.setToolTip("툴팁 입니다.<b>안녕하세요.<b\>")    # 마우스 오버시 툴팁 표시
        btn.move(25, 30)

        self.setGeometry(100, 100, 400, 500)    # 위치 위로부터, 왼쪽으로 부터, 가로사이즈, 세로사이즈
        self.setWindowTitle("첫번째 학습 시간")
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec())