# 0导入需要的包、模块
import os
import sys
from PyQt5.Qt import *


class MyLineEdit(QLineEdit):

    def mousePressEvent(self, ev):
        super().__init__()

        print(ev)
        res = QFileDialog.getOpenFileName(
            self,
            "选择一个py文件",
            "./",
            "All(*.*);;Images(*.png);;Python文件(*.py)",
            "Python文件(*.py)"

        )
        print(res)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        print('test')
        self.setWindowTitle("win_title")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(200, 100)
        label.setText('filename')
        label.resize(200, 90)
        self.label = label
        label.setVisible(False)

        btn2 = QPushButton("选择一个文件", self)
        btn2.setStyleSheet(
            "color: red"
        )

        btn2.clicked.connect(self.fn)

        btn3 = QPushButton("删除", self)
        btn3.move(200, 90)
        btn3.setStyleSheet(
            "color: red"
        )
        btn3.clicked.connect(lambda: self.label.setVisible(False))

    def fn(self, v):
        res, _ = QFileDialog.getOpenFileName(
            self,
            "选择一个py文件",
            "./",
            "All(*.*);;Images(*.png);;Python文件(*.py)",
            "Python文件(*.py)"

        )
        print(res)
        _, file_name = os.path.split(res)
        print(file_name)
        self.label.setText(file_name)
        self.label.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())