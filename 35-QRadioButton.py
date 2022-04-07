# 0 导入需要的包和模块
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup

# 1 创建一个应用程序对象
app = QApplication(sys.argv)


# 2 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("win_tt")
window.resize(500, 500)

red = QWidget(window)
red.resize(150, 150)
red.setStyleSheet("background-color: red;")
red.move(50, 50)

green = QWidget(window)
green.resize(150, 150)
green.setStyleSheet("background-color: green;")
green.move(red.x() + red.width(), red.y() + red.width())

male_rb = QRadioButton("男", red)
male_rb.move(10, 10)
male_rb.setChecked(True)
male_rb.setShortcut("Alt+M")

female_rb = QRadioButton("女-&Female", red)
female_rb.move(10, 50)

female_rb.setIcon(QIcon("a.png"))
female_rb.setIconSize(QSize(60, 60))
female_rb.toggled.connect(lambda is_checked: print(is_checked))

sex_group = QButtonGroup(window)
sex_group.addButton(male_rb, 1)
sex_group.addButton(female_rb, 2)

# 不互斥
# female_rb.setAutoExclusive(False)


# 2.3 展示控件

rb_ok = QRadioButton("ok", green)
rb_ok.move(30, 10)
rb_ok.setChecked(True)
rb_no = QRadioButton("no", green)
rb_no.move(30, 60)

yes_group = QButtonGroup(window)
yes_group.addButton(rb_ok, 3)
yes_group.addButton(rb_no, 4)

yes_group.setId(rb_ok, 1)
yes_group.setId(rb_no, 2)

print(yes_group.id(rb_ok))
print(yes_group.id(rb_no))
print(yes_group.checkedId())

# sex_group.removeButton(female_rb)
#
# print(sex_group.buttons())
# print(sex_group.button(2))
# print("选中了", sex_group.checkedButton())


window.show()
# 3 执行应用程序，进入消息循环
sys.exit(app.exec_())