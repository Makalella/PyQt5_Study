
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lbl1 = QLabel("Zetcode", self)
#         lbl1.move(15, 10)
#
#         lbl2 = QLabel("tutorials", self)
#         lbl2.move(35, 40)
#
#         lbl3 = QLabel("for programmers", self)
#         lbl3.move(55, 70)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Absolute")
#         self.show()

# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
#                                                 #수직으로       #수평으로
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch()
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle("Buttons")
#         self.show()

# import sys
# from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         names = ["Cls", "Bck", "", "Close",
#                  "7", "8", "9", "/",
#                  "4", "5", "6", "*",
#                  "1", "2", "3", "-",
#                  "0", ".", "=", "+"]
#
#         positions = [(i, j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#             if name == "":
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#
#         self.move(300, 150)
#         self.setWindowTitle("calculator")
#         self.show()

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 6, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Review")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())