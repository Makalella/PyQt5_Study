
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("Hello.")

        # 메뉴바 생성
        menu = self.menuBar()

        # 그룹 생성
        menu_file = menu.addMenu("File")
        menu_edit = menu.addMenu("Edit")
        menu_view = menu.addMenu("View")

        # File 그룹 하위 생성
        file_new = QMenu("New", self)
        new_txt = QAction("Text File", self)
        new_py = QAction("Python File", self)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        file_exit = QAction("Exit", self)
        file_exit.setShortcut("Ctrl+q")
        file_exit.setStatusTip("Bye")
        # file_exit.triggered.connect(QCoreApplication.instance().quit)
        file_exit.triggered.connect(qApp.quit)

        # File 그룹에 추가
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)

        # View 그룹 하위에 체크 박스 생성
        view_stat = QAction("Status Bar", self, checkable = True)
        view_stat.setChecked(True)  # 초기 상태가 Check 되어 있음
        view_stat.triggered.connect(self.tglStat)

        # View 그룹에 추가
        menu_view.addAction(view_stat)


        # Window 설정
        self.resize(450, 400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)
        quit = cm.addAction("Quit")
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            # QCoreApplication.instance().quit
            qApp.quit()
        else:
            pass


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())