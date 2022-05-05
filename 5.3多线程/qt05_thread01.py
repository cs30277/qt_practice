# 0导入需要的包、模块
import sys
from PyQt5.Qt import *


sec = 0


def set_time():
    global sec
    sec += 1
    lcdNumber.display(sec)

def work():
    timer.start(1000)
    for i in range(20000000):
        pass
    timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    lcdNumber = QLCDNumber()
    btn = QPushButton('测试')
    btn.clicked.connect(work)

    v_layout = QVBoxLayout(top)
    v_layout.addWidget(lcdNumber)
    v_layout.addWidget(btn)

    timer = QTimer()
    timer.timeout.connect(set_time)

    top.show()
    sys.exit(app.exec_())