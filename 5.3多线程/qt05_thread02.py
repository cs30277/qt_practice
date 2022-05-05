# -*- coding: utf-8 -*-
'''
    【简介】
    PyQT5中 QTimer例子


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0

class WorkThread(QThread):
    sig = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(2000000000):
            pass
        self.sig.emit()


def count_time():
    global sec
    sec += 1
    lcdNumber.display(sec)


def work():
    timer.start(1000)
    work_thread.start()
    work_thread.sig.connect(time_stop)


def time_stop():
    timer.stop()
    print('运行结束用时', lcdNumber.value())
    global sec
    sec = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    lcdNumber = QLCDNumber()
    btn = QPushButton('测试')

    v_layout = QVBoxLayout(top)
    v_layout.addWidget(lcdNumber)
    v_layout.addWidget(btn)

    timer = QTimer()
    work_thread = WorkThread()
    btn.clicked.connect(work)
    timer.timeout.connect(count_time)

    top.show()
    sys.exit(app.exec_())


