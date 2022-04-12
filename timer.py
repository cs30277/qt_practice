from PyQt5.Qt import *
import sys


class MyObject(QObject):
    # def timerEvent(self, a0: 'QTimerEvent') -> None:
    def timerEvent(self, evt):
        print(evt, "1")


class Mylabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 22px")
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        cur_sec = int(self.text())
        cur_sec -= 1
        self.setText(str(cur_sec))

        if cur_sec == 0:
            self.killTimer(self.timer_id)

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

# obj = MyObject()
# time_id = obj.startTimer(1000)
#
# obj.killTimer(time_id)

label = Mylabel(window)



window.show()
sys.exit(app.exec_())