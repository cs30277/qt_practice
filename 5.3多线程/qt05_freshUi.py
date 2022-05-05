import sys
import time
from PyQt5.Qt import *


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('实时刷新页面')
        self.list_file = QListWidget()
        self.btn_start = QPushButton('开始')
        self.btn_start.clicked.connect(self.slot_add)

        g_layout = QGridLayout(self)
        g_layout.addWidget(self.list_file, 0, 0, 1, 2)
        g_layout.addWidget(self.btn_start, 1, 1)
        self.setLayout(g_layout)

    def slot_add(self):
        for i in range(10):
            str_n = 'File index {}'.format(i)
            self.list_file.addItem(str_n)
            QApplication.processEvents()
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())