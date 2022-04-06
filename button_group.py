import sys

# from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QButtonGroup

# 1 创建应用程序对象

app = QApplication(sys.argv)

# 2 控件操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("win_title")
window.resize(500, 500)

label1 = QLabel(window)
label1.setText("sex")

male_rd = QRadioButton("male", window)
female_rd = QRadioButton("female", window)

sex_group = QButtonGroup(window)
sex_group.addButton(male_rd)
sex_group.addButton(female_rd)

sex_layout = QHBoxLayout()
sex_layout.addWidget(male_rd)
sex_layout.addWidget(female_rd)

p_rd = QRadioButton("python", window)
c_rd = QRadioButton("C", window)

like_group = QButtonGroup(window)
like_group.addButton(p_rd)
like_group.addButton(c_rd)

like_label = QLabel('like', window)

like_layout = QHBoxLayout()
like_layout.addWidget(like_label)
like_layout.addWidget(p_rd)
like_layout.addWidget(c_rd)


main_layout = QGridLayout()
main_layout.addWidget(label1, 0, 0, 1, 1)
main_layout.addLayout(sex_layout, 0, 1, 1, 1, Qt.AlignLeft)
main_layout.addWidget(label1, 1, 0, 1, 1)
main_layout.addLayout(like_layout, 1, 1, 1, 1)
window.setLayout(main_layout)

# 2.3展示控件
window.show()
# 3 应用程序执行，进入消息循环
sys.exit(app.exec_())