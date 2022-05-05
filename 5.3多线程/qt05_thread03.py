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
        self.thread = Worker()
        self.thread.sig_out.connect(self.slot_add)

        self.list_file = QListWidget()
        self.btn_start = QPushButton('开始')
        self.btn_start.clicked.connect(self.slot_start)

        g_layout = QGridLayout(self)
        g_layout.addWidget(self.list_file, 0, 0, 1, 2)
        g_layout.addWidget(self.btn_start, 1, 1)

    def slot_add(self, file_inif):
        self.list_file.addItem(file_inif)

    def slot_start(self):
        self.btn_start.setEnabled(False)
        self.thread.start()


class Worker(QThread):
    sig_out = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            file_str = 'File index {}'.format(self.num)
            self.num += 1
            self.sig_out.emit(file_str)
            self.sleep(2)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())