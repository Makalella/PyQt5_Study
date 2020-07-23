
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar()                   # 메뉴 생성

        menu_file = menu.addMenu("File")        # 그룹1 생성

        file_new = QMenu("New", self)
        new_txt = QAction("텍스트파일", self)
        new_py = QAction("파이썬파일", self)

        menu_file.addMenu(file_new)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        file_exit = QAction("Exit", self)       # 메뉴 객체 생성
        file_exit.setShortcut("Ctrl+q")
        file_exit.setStatusTip("누르면 종료")
        file_exit.triggered.connect(QCoreApplication.instance().quit)

        menu_file.addAction(file_exit)

        menu_edit = menu.addMenu("Edit")        # 그룹2 생성

        self.resize(450, 500)
        self.show()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec())