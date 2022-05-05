# 0导入需要的包、模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("win_title")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.list_file = QListWidget()
        self.label = QLabel('显示当前时间')

        self.start_btn = QPushButton('开始')
        self.start_btn.clicked.connect(self.start_timer)
        self.end_btn = QPushButton('结束')
        self.end_btn.clicked.connect(self.end_timer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)

        g_layout = QGridLayout(self)
        g_layout.addWidget(self.label, 0, 0, 1, 2)
        g_layout.addWidget(self.start_btn, 1, 0)
        g_layout.addWidget(self.end_btn, 1, 1)
        self.setLayout(g_layout)

    def show_time(self):
        time = QDateTime.currentDateTime()
        time_display = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(time_display)

    def start_timer(self):
        self.timer.start(1000)
        self.start_btn.setEnabled(False)
        self.end_btn.setEnabled(True)

    def end_timer(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.end_btn.setEnabled(False)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())