import sys
from PyQt5.Qt import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=128><b>Hello PyQt，窗口会在10秒内消失</b></font>")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()

    QTimer.singleShot(10000, app.quit)
    sys.exit(app.exec_())